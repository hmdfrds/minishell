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

        try:
            subprocess.run(args, check=False, shell=True)
        except FileNotFoundError:
            print(f"minishell: command not found: {args[0]}")
        except Exception as e:
            print(f"minishell: error executing command: {e}")

    except EOFError:
        break

print("\n Exiting minishell.")
