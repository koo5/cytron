#!/usr/bin/python3
# -*- coding: utf-8 -*-

program_text = """

libraries:
  pygame:
    functions:
      create pygame window:
      - command:
          namespace: builtin
          command: print
          argument: "create pygame window"
      - command:
          namespace: pygame
          command: ensure pygame is initialized

      ensure pygame is initialized:
      - control:
          structure: if
          condition:
            type: flag
            namespace: pygame
            name: is pygame initialized?
          false:
          - command:
              namespace: builtin
              command: print
              argument: "initializing pygame"
          - command:
              namespace: python
              exec: |
                import pygame
                pygame_window = pygame.display.set_mode([400, 300])
          - set:
              what:
                pygame window
              to:
                extract:
                  expression: pygame_window
              

commands:
- command:
    namespace: builtin
    command: print
    argument: "hello"
- command:
    namespace: builtin
    command: print
    argument: "world"

- command:
    namespace: pygame
    command: create pygame window

"""

python_env = dict()

import yaml

program = yaml.load(program_text)

print (program)

def run_list(statements):
	for statement in statements:
		run(statement)


def run(statement):
	print (statement)
	if statement['command']:
		command = statement['command']

		if command['namespace'] == 'builtin':
			if command['command'] == 'print':
				print(command['argument'])

		elif command['namespace'] in program['libraries']:
			if command['command'] in program['libraries'][command['namespace']]['functions']:
				run_list(program['libraries'][command['namespace']]['functions'][command['command']])


for statement in program['commands']:
	print (statement)
	run(statement)
