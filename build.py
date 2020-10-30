#!/usr/bin/env python3

import os
import sys
import subprocess
import shutil

built_images = []

README_TEMPLATE = '''
# CTF Tools 
Just a collection of some dockerfiles to help streamline the scramble of getting stable tools during a CTF! Contributions are always welcome :) 

Each tool is supposed to be a passthrough so after running `python3 build.py` to build and stock your docker registery, you can do things like `./bin/nmap -sV some.host` without having to install/build things in your local environment (which increases the security of your computer measurably as well while participating).

## Building
You should be able to just clone this repo, then run `python3 build.py`, which will build all the docker images found in this repo, then regenerate the scripts in the `bin/` directory.

## Current tools:
{}

'''

if os.path.exists('bin/'):
	shutil.rmtree('bin/')
	os.mkdir('bin/')

for docker_file in os.listdir('dockerfiles/'):
	image_name = docker_file.split('.')[-1]

	docker_file_path = os.path.join('dockerfiles', docker_file)

	build_string = ['docker', 'build', '-t', image_name, '-f', docker_file_path, '.']

	print("Building image for {} (executing '{}')".format(image_name.title(), " ".join(build_string)))

	result = subprocess.run(build_string, capture_output=True)

	if result.returncode != 0:
		print("Error building {}!".format(image_name))
		print("STDOUT: " + result.stdout.decode())
		print("STDERR:\n{}\n".format(result.stderr.decode()))
		sys.exit(1)

	bin_file = 'bin/{}'.format(image_name)

	with open(bin_file, 'w') as f:
		f.write('''
#!/usr/bin/env bash

set -ex

docker run --rm -it -v "$(pwd)":/shared {} "$@" || echo 'Error starting docker or something went wrong! Do you have the images installed locally?'
		'''.format(image_name).strip())

	os.chmod(bin_file, 0o755)

	built_images.append(image_name)

with open('README.md', 'w') as f:
	f.write(README_TEMPLATE.format(''.join(['- [{}](dockerfiles/Dockerfile.{})\n'.format(x.title(), x) for x in built_images])))

print("\nDone! Built {}\n".format(built_images))
