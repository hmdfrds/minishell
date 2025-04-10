import subprocess
import sys

while True:
    print("minishell> ", end="")
    sys.stdout.flush()
    try:
        command_line = input()
    except EOFError:
        break

print("\n Exiting minishell.")
