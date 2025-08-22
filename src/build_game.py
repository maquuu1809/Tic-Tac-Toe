import subprocess
import os
import sys
sys.path.append(os.path.dirname(__file__))
from create_shortcut import create_shortcut

game_path = os.path.join(os.path.dirname(__file__), "game", "main.py")
icon_path = os.path.join(os.path.dirname(__file__), "..", "images", "icon.ico")

def build_game(game_path):
    if not os.path.exists(game_path):
        print("❌ File not found: ", game_path)
        return

    try:
        print("🚀 Building game...")
        subprocess.run([
            sys.executable, "-m", "PyInstaller",
            f"--icon={icon_path}",
            "--name=Tic-Tac-Toe",
            "--onefile",
            "--noconsole",
            game_path
        ], check=True)

        dist_path = os.path.join("dist", "Tic-Tac-Toe.exe")
        if os.path.exists(dist_path):
            print("✅ Icon created in: ", dist_path)
            create_shortcut(dist_path, "Tic-Tac-Toe")
        else:
            print("⚠️ Build finished, but .exe not found in /dist")
    except subprocess.CalledProcessError:
        print("❌ Building game failed.")
    except Exception as e:
        print("❌ Error: ", str(e))

if __name__ == "__main__":
    build_game(game_path)
