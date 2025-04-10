import subprocess
import sys

while True:
    print("minishell> ", end="")
    sys.stdout.flush()
    try:
        command_line = input()

        args = command_line.split()
        
        if not args:
            continue
        
        if args[0] == "exit":
            break

    except EOFError:
        break

print("\n Exiting minishell.")
