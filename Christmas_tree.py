import time
import random
import sys
import os

# 색상 및 커서 제어 코드
COLORS = [
    '\033[91m',  # Red
    '\033[92m',  # Green
    '\033[93m',  # Yellow
    '\033[94m',  # Blue
    '\033[95m',  # Magenta
    '\033[96m',  # Cyan
    '\033[97m',  # White
]
RESET = '\033[0m'
HIDE_CURSOR = '\033[?25l'  # 커서 숨김
SHOW_CURSOR = '\033[?25h'  # 커서 보이기
MOVE_TO_TOP = '\033[H'  # 커서를 맨 위(좌측 상단)로 이동

tree_shape = [
    "         * ",
    "        *** ",
    "       ***** ",
    "      ******* ",
    "     ********* ",
    "    *********** ",
    "   ************* ",
    "  *************** ",
    " ***************** ",
    "*******************",
    "       | | |       ",
    "       | | |       "
]

lyrics_data = [
    ("Last Christmas", 2.5),
    ("I gave you my heart", 2.5),
    ("But the very next day", 2.5),
    ("You gave it away", 2.0),
    ("", 0.5),
    ("This year", 1.5),
    ("To save me from tears", 2.5),
    ("I'll give it to someone special", 3.5),
    ("", 1.0),
    ("A face on a lover", 2.5),
    ("With a fire in his heart", 2.5),
    ("A man undercover", 2.5),
    ("But you tore me apart", 3.0),
    ("Merry Christmas!", 5.0)
]


def animate_tree():
    # 1. 화면을 완전히 깨끗하게 지움 (최초 1회)
    os.system('cls' if os.name == 'nt' else 'clear')

    # 커서 숨기기
    print(HIDE_CURSOR, end="")

    start_time = time.time()
    lyric_index = 0
    current_lyric_start = start_time

    try:
        while True:
            # 2. 커서를 무조건 화면 맨 위로 보냄 (화면 지우기 X -> 깜빡임 없음)
            # 버퍼에 담아서 한 번에 출력 (속도 향상 및 끊김 방지)
            buffer = MOVE_TO_TOP + "\n"  # 맨 위에서 한 줄 띄우기

            # 가사 계산 로직
            current_time = time.time()
            if lyric_index < len(lyrics_data):
                text, duration = lyrics_data[lyric_index]
                if current_time - current_lyric_start > duration:
                    lyric_index += 1
                    current_lyric_start = current_time
                    current_lyric_text = ""
                else:
                    current_lyric_text = text
            else:
                current_lyric_text = "Happy Holidays!"

            # 트리 그리기
            for i, line in enumerate(tree_shape):
                row_str = ""
                for char in line:
                    if char == '*':
                        row_str += random.choice(COLORS) + char + RESET
                    elif char == '|':
                        row_str += '\033[33m' + char + RESET
                    else:
                        row_str += char

                # 가사 출력 (잔상 제거를 위해 뒤에 공백 40칸 확보)
                if i == 5:
                    padded_lyric = f"{current_lyric_text:<40}"
                    row_str += f"   \033[1m\033[97m{padded_lyric}\033[0m"

                buffer += row_str + "\n"

            # 3. 화면에 한 번에 뿌리기
            sys.stdout.write(buffer)
            sys.stdout.flush()

            time.sleep(0.15)

    except KeyboardInterrupt:
        print(SHOW_CURSOR)
        print("\nStopped.")
        sys.exit()
    finally:
        print(SHOW_CURSOR)


if __name__ == "__main__":
    animate_tree()
