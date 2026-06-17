#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fsociety_quest.py — День рождения Саши
Запуск: python fsociety_quest.py
"""

import sys
import time
import os
import random
import threading
import textwrap
import webbrowser

try:
    import colorama
    colorama.init(autoreset=True)
    from colorama import Fore, Back, Style
except ImportError:
    os.system("pip install colorama -q")
    import colorama
    colorama.init(autoreset=True)
    from colorama import Fore, Back, Style

# ── цвета ──────────────────────────────────────────────────────────────────
G   = Fore.GREEN
BG  = Fore.LIGHTGREEN_EX
C   = Fore.CYAN
Y   = Fore.YELLOW
R   = Fore.RED
M   = Fore.MAGENTA
W   = Fore.WHITE
DIM = Fore.BLACK + Style.BRIGHT
RST = Style.RESET_ALL

MASK = r"""
                                                                             
  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM       
  MMMMMMMMMMMMMMMMMMssssssssssssssssssssssssssMMMMMMMMMMMMMMMMMMMMM          
  MMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMM          
  MMMMMMMMMMyy''                                    ''yyMMMMMMMMMM          
  MMMMMMMMyy''                                          ''yyMMMMMM          
  MMMMMMy''                                                    ''yMMMM         
  MMMy'                                                         'yMMM        
  Mh'                                                             'hM        
  -                                                                 -        
                                                                             
  ::                                                               ::        
  MMhh.        ..hhhhhh..                      ..hhhhhh..        .hhMM       
  MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM       
  ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---       
  MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM       
  ---mMM ''               'mmMMMMMM  MMMMMMMMmm'             '' MMm---       
  yyyym'    .               'mMMMMm'  'mMMMMm'              .    'myyyy       
  mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm       
          MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM               
          N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N               
           +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +               
              o+++     ++++Mo    M      M    oM++++     +++o                 
                                oo      oo                                   
          oM                  oo          oo                Mo               
        oMMo                 M              M               oMMo             
      +MMMM                  s              s                  MMMM+            
     +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+          
     +MMMMMMM+        ++NNMMMMMMMMN+    +NMMMMMMMMNN++        +MMMMMMM+        
     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM        
     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy        
   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m      
   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM      
   MMMm .yyMMMMMMMMMMMMMMMM      MMMMMMMMMM      MMMMMMMMMMMMMMMMyy. mMMM      
   MMMMd   ''''hhhhh        odddo          obbbo        hhhh''''   dMMMM      
   MMMMMd               'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM      
   MMMMMMd               'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM      
   MMMMMMM-                ''ddMMMMMMMMMMMMMMdd''                -MMMMMMM      
   MMMMMMMM                    '::dddddddd::'                    MMMMMMMM      
   MMMMMMMM-                                                   -MMMMMMMM      
   MMMMMMMMM                                                   MMMMMMMMM      
   MMMMMMMMMy                                                 yMMMMMMMMM      
   MMMMMMMMMMy.                                             .yMMMMMMMMMM      
   MMMMMMMMMMMMy.                                         .yMMMMMMMMMMMM      
   MMMMMMMMMMMMMMy.                                     .yMMMMMMMMMMMMMM      
   MMMMMMMMMMMMMMMMs.                                 .sMMMMMMMMMMMMMMMM      
   MMMMMMMMMMMMMMMMMMss.               ....           .ssMMMMMMMMMMMMMMMMMM      
   MMMMMMMMMMMMMMMMMMMMNo         oNNNNo         oNMMMMMMMMMMMMMMMMMMMMMM    
"""

LOGO = r"""
   .o88o.                               o8o                 .
   888 `"                               `"'               .o8
  o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
   888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
   888    `Y88b.  888   888 888        888  888ooo888   888     `88..8'
   888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
  o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'
                                                                .o...P'
                                                                `XER0'
"""

STAGES = [
    # (тип, название, описание, зашифровано, ответ, подсказка)
    ("start", "ИНИЦИАЛИЗАЦИЯ", "", "", "start",
     "Просто введи: start"),

    ("base64", "BASE64", "Это слово зашифровано в Base64. Расшифруй и напиши, что получилось:",
     "aGFja2Vy", "hacker",
     "Любой Base64-декодер (например, base64decode.org) превратит aGFja2Vy в hacker."),

    ("rot13", "ROT13 ШИФР", "Каждая буква здесь сдвинута на 13 позиций по алфавиту. Сдвинь обратно:",
     "RYYV BG", "elliot",
     "ROT13 работает одинаково в обе стороны: RYYV BG → ELLIOT → elliot."),

    ("hex", "HEX → ТЕКСТ", "Каждая пара символов — это код одной буквы в HEX. Переведи в обычный текст:",
     "66 73 6F 63 69 65 74 79", "fsociety",
     "66=f 73=s 6F=o 63=c 69=i 65=e 74=t 79=y → fsociety"),

    ("morse", "АЗБУКА МОРЗЕ", "Перед тобой сообщение в азбуке Морзе. Расшифруй его:",
     ".... .- -.-. -.-", "hack",
     "H=.... A=.- C=-.-. K=-.- → hack"),

    ("binary", "ДВОИЧНЫЙ КОД", "Это слово записано в двоичном коде — только 0 и 1. Переведи в текст:",
     "01110010 01101111 01101111 01110100", "root",
     "01110010=r 01101111=o 01101111=o 01110100=t → root"),

    ("atbash", "ШИФР АТБАШ", "В этом шифре алфавит читается в обратную сторону: A↔Z, B↔Y, C↔X и так далее. Расшифруй слово:",
     "ILYLG", "robot",
     "Атбаш меняет первую букву алфавита на последнюю, вторую — на предпоследнюю и т.д. ILYLG → ROBOT."),

    ("caesar", "ШИФР ЦЕЗАРЯ", "Шифр Цезаря со сдвигом 3: каждая буква сдвинута на 3 вперёд. Сдвинь обратно:",
     "HDFNHG", "hacked",
     "Сдвигаем каждую букву на 3 назад: H-3=E D-3=A F-3=C N-3=K H-3=E G-3=D → hacked."),

    ("ascii", "ASCII КОДЫ", "Эти числа — это ASCII-коды букв. Переведи их в слово:",
     "77 97 116 114 105 120", "matrix",
     "77=M 97=a 116=t 114=r 105=i 120=x → matrix"),

    ("nato", "ФОНЕТИЧЕСКИЙ АЛФАВИТ", "Перед тобой слова фонетического алфавита — как у пилотов и радистов. Возьми первую букву каждого слова:",
     "FOXTROT ROMEO ECHO ECHO DELTA OSCAR MIKE", "freedom",
     "F-oxtrot R-omeo E-cho E-cho D-elta O-scar M-ike → freedom"),

    ("name", "ФИНАЛЬНАЯ АУТЕНТИФИКАЦИЯ",
     "Как зовут твоего друга, который сделал этот квест?",
     "", None,
     "Введи имя человека, который подарил тебе этот квест."),
]

# ── утилиты ─────────────────────────────────────────────────────────────────

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ── easing-функции ───────────────────────────────────────────────────────────

def ease_in_out(t):
    """Кубическая ease-in-out (плавный старт и конец)"""
    return t * t * (3 - 2 * t)

def ease_out(t):
    """Квадратичная ease-out (плавное торможение)"""
    return 1 - (1 - t) ** 2

# ── анимации текста ──────────────────────────────────────────────────────────

def slow_print(text, color=G, delay=0.012, newline=True):
    """Плавный посимвольный вывод с fade-in ускорением."""
    n = len(text)
    for i, ch in enumerate(text):
        t = ease_out(i / max(n - 1, 1))
        d = delay * (1.8 - t)          # начало чуть медленнее, потом разгон
        sys.stdout.write(color + ch + RST)
        sys.stdout.flush()
        time.sleep(max(d, 0.004))
    if newline:
        print()

def instant(text, color=G):
    print(color + text + RST)

def fade_in_line(text, color=G, steps=6, total_time=0.18):
    """Имитация fade-in: строка появляется плавно через смену яркости."""
    fade_colors = [DIM, DIM, color, color, color, color]
    step_delay = total_time / steps
    for i, fc in enumerate(fade_colors):
        sys.stdout.write('\r' + fc + text + RST)
        sys.stdout.flush()
        time.sleep(step_delay)
    print()

def reveal_block(lines, color=G, line_delay=0.04):
    """Блок строк появляется сверху вниз с плавным нарастанием."""
    total = len(lines)
    for i, line in enumerate(lines):
        t = ease_in_out(i / max(total - 1, 1))
        d = line_delay * (1 - t * 0.5)
        instant(line, color)
        time.sleep(d)

def blink_text(text, color=Y, times=3, interval=0.3):
    for _ in range(times):
        sys.stdout.write(color + text + RST + '\r')
        sys.stdout.flush()
        time.sleep(interval)
        sys.stdout.write(' ' * len(text) + '\r')
        sys.stdout.flush()
        time.sleep(interval)
    print(color + text + RST)

# ── прогресс-бар ─────────────────────────────────────────────────────────────

def progress_bar(current, total, width=50, animated=True):
    """Прогресс-бар с плавным заполнением при первом показе."""
    if animated and current > 0:
        prev = current - 1
        prev_filled = int(width * prev / total)
        target_filled = int(width * current / total)
        steps = max(target_filled - prev_filled, 1)
        for step in range(steps + 1):
            filled = prev_filled + step
            bar = '█' * filled + '▓' * min(1, target_filled - filled) + '░' * (width - filled - min(1, target_filled - filled))
            bar = bar[:width]
            pct = int(100 * current / total)
            sys.stdout.write(G + f"\r  [{bar}] {pct}% ({current}/{total})" + RST)
            sys.stdout.flush()
            time.sleep(0.018)
        print()
    else:
        filled = int(width * current / total)
        bar = '█' * filled + '░' * (width - filled)
        pct = int(100 * current / total)
        print(G + f"  [{bar}] {pct}% ({current}/{total})" + RST)

# ── matrix rain ──────────────────────────────────────────────────────────────

def matrix_rain(seconds=2):
    """Matrix-дождь с плавным fade in/out через яркость."""
    chars = "アイウエオカキクケコサシスセソタチツテトナニヌネノ0123456789ABCDEF"
    total = time.time() + seconds
    t0 = time.time()
    while time.time() < total:
        elapsed = time.time() - t0
        # fade in первые 0.3 с, fade out последние 0.3 с
        if elapsed < 0.3:
            ratio = elapsed / 0.3
        elif seconds - elapsed < 0.3:
            ratio = (seconds - elapsed) / 0.3
        else:
            ratio = 1.0
        ratio = max(0.1, ratio)
        line_len = int(70 * ratio)
        line = ''.join(random.choice(chars) if random.random() > 0.3 else ' ' for _ in range(line_len))
        color = BG if random.random() > 0.85 else DIM
        print(color + line + RST)
        time.sleep(0.05)

# ── boot sequence ─────────────────────────────────────────────────────────────

def boot_sequence():
    clear()
    lines = [
        (DIM,  "[BOOT]   KERNEL 4.19.0-fsociety ............. OK"),
        (DIM,  "[INIT]   SERVICES ............................ STARTED"),
        (R,    "[SEC]    FIREWALL ............................ BYPASSED"),
        (DIM,  "[NET]    TOR RELAY x7 ........................ ESTABLISHED"),
        (DIM,  "[CRYPT]  AES-256 ENGINE ...................... LOADED"),
        (Y,    "[TARGET] SASHA ............................... IDENTIFIED"),
        (G,    "[QUEST]  BIRTHDAY_PROTOCOL ................... ACTIVATED"),
    ]
    for color, line in lines:
        slow_print(line, color, delay=0.008)
        time.sleep(0.07)
    time.sleep(0.4)
    print()
    matrix_rain(1.5)

# ── маска и логотип ───────────────────────────────────────────────────────────

def show_mask():
    lines = MASK.split('\n')
    total = len(lines)
    for i, line in enumerate(lines):
        t = ease_in_out(i / max(total - 1, 1))
        print(G + line + RST)
        time.sleep(max(0.002, 0.007 * (1 - t * 0.6)))

def show_logo():
    lines = LOGO.split('\n')
    for i, line in enumerate(lines):
        print(BG + line + RST)
        time.sleep(0.004)
    time.sleep(0.15)

# ── BSOD (при попытке выхода) ─────────────────────────────────────────────────

def bsod():
    clear()
    print(Back.BLUE + Fore.WHITE + Style.BRIGHT)
    w = 78
    def bline(text="", center=False):
        if center:
            text = text.center(w)
        else:
            text = text.ljust(w)
        print(" " + text)

    print(" " + " " * w)
    bline()
    bline("   :)", )
    bline()
    bline("   ПК ВЫНУЖДЕН ПЕРЕЗАПУСТИТЬСЯ", )
    bline()
    bline("   Обнаружена попытка выйти из квеста.")
    bline("   Это СТРОГО ЗАПРЕЩЕНО протоколом fsociety.")
    bline()
    bline("   С Днём Рождения, Саша! Тебе не сбежать.")
    bline("   Пройди квест — тогда получишь свободу. :)")
    bline()
    bline()
    bline("   STOP: 0x000000BD_BIRTHDAY_DETECTED")
    bline("   fsociety.sys — QUEST_NOT_COMPLETED")
    bline()
    for i in range(5, 0, -1):
        sys.stdout.write(Back.BLUE + Fore.WHITE + Style.BRIGHT +
                         f"   Автоматический возврат через {i} сек...".ljust(w) + "\r")
        sys.stdout.flush()
        time.sleep(1)
    print(RST)

# ── победный экран ────────────────────────────────────────────────────────────

def show_win(friend_name):
    clear()
    print()
    matrix_rain(1.2)
    print()

    win_art = [
        C + "╔═══════════════════════════════════════════════════════════╗",
        C + "║                                                           ║",
        C + "║   ██████╗  ██████╗  ██████╗  ██╗██╗                      ║",
        C + "║   ██╔══██╗██╔═══██╗██╔═══██╗██╔╝██║                      ║",
        C + "║   ██║  ██║██║   ██║██║   ██║███╗╚═╝                      ║",
        C + "║   ██║  ██║██║   ██║██║   ██║██╔╝██╗                      ║",
        C + "║   ██████╔╝╚██████╔╝╚██████╔╝██║ ╚═╝                      ║",
        C + "║                                                           ║",
        C + "╚═══════════════════════════════════════════════════════════╝",
    ]
    reveal_block(win_art, color="", line_delay=0.05)
    print()
    slow_print("  ВСЕ 10 УРОВНЕЙ ПРОЙДЕНЫ. ДОСТУП ОТКРЫТ.", Y, delay=0.025)
    print()
    time.sleep(0.3)
    slow_print("  Саша,", W, delay=0.04)
    print()
    slow_print("  ты только что доказал, что ты — настоящий хакер.", W, delay=0.03)
    slow_print("  10 шифров. 10 уровней. Ни одна система не устояла.", W, delay=0.03)
    print()
    time.sleep(0.4)
    slow_print('  "We are fsociety. We are finally free.', C, delay=0.03)
    slow_print('   We are finally awake."', C, delay=0.03)
    instant("                          — Mr. Robot, season 1", DIM)
    print()
    time.sleep(0.5)
    blink_text(f"  С ДНЁМ РОЖДЕНИЯ ОТ {friend_name.upper()}!  🎂🎉", M, times=4, interval=0.35)
    print()
    slow_print("  Пусть этот год взломает все твои ограничения", W, delay=0.03)
    slow_print("  и откроет доступ к новым уровням жизни!", W, delay=0.03)
    print()
    instant("  [ПРОТОКОЛ DR_SASHA ЗАВЕРШЁН] [КЛЮЧ: СВОБОДА]", DIM)
    instant("  [fsociety out]", DIM)
    print()
    time.sleep(2)

    # ── ФИНАЛЬНЫЙ ЭКРАН: цифры 4928 на весь экран ───────────────────────────
    clear()
    print(Back.BLUE + Fore.WHITE + Style.BRIGHT)

    digits_art = [
        "  ██╗  ██╗ █████╗  █████╗  █████╗  ",
        "  ██║  ██║██╔══██╗██╔══██╗██╔══██╗ ",
        "  ███████║╚██████║╚██████║╚╚█████╔╝ ",
        "  ╚════██║ ╚═══██║ ╚═══██║ ██╔══██╗ ",
        "       ██║ █████╔╝ █████╔╝ ╚█████╔╝ ",
        "       ╚═╝ ╚════╝  ╚════╝   ╚════╝  ",
    ]

    # Блок цифр 4 9 2 8 в ASCII-арт
    four = [
        "██╗  ██╗",
        "██║  ██║",
        "███████║",
        "╚════██║",
        "     ██║",
        "     ╚═╝",
    ]
    nine = [
        " █████╗ ",
        "██╔══██╗",
        "╚██████║",
        " ╚═══██║",
        " █████╔╝",
        " ╚════╝ ",
    ]
    two = [
        "██████╗ ",
        "╚════██╗",
        " █████╔╝",
        "██╔═══╝ ",
        "███████╗",
        "╚══════╝",
    ]
    eight = [
        " █████╗ ",
        "██╔══██╗",
        "╚█████╔╝",
        "██╔══██╗",
        "╚█████╔╝",
        " ╚════╝ ",
    ]

    w = 78
    gap = "    "
    print()
    print()
    print()
    print()
    for row in range(6):
        line = gap + four[row] + gap + nine[row] + gap + two[row] + gap + eight[row]
        print(Back.BLUE + Fore.WHITE + Style.BRIGHT + line.center(w))
    print()
    print()
    press = "[ Нажми Enter, чтобы открыть сюрприз ]"
    print(Back.BLUE + Fore.WHITE + Style.BRIGHT + press.center(w))
    print()
    print(RST, end="")

    input()
    webbrowser.open("https://github.com/fsociety00protocol/neratkadlyasashi")

# ── промпт ввода ──────────────────────────────────────────────────────────────

def get_prompt(stage_num):
    prompts = {
        0:  "root@fsociety:~$",
        1:  "base64@level1:~$",
        2:  "rot13@level2:~$",
        3:  "hex@level3:~$",
        4:  "morse@level4:~$",
        5:  "binary@level5:~$",
        6:  "atbash@level6:~$",
        7:  "caesar@level7:~$",
        8:  "ascii@level8:~$",
        9:  "nato@level9:~$",
        10: "final@auth:~$",
    }
    return prompts.get(stage_num, "root@fsociety:~$")

# ── заголовок уровня (переработанное меню) ───────────────────────────────────

def show_stage_header(idx, stype, name, desc, encoded):
    """
    Современный, чистый заголовок уровня.
    Уровень 0 (start) — без заголовка.
    """
    print()
    if idx == 0:
        return

    total_levels = len(STAGES) - 1   # 10

    # ── верхний разделитель ──
    sep = "─" * 58
    instant(f"  {DIM}{sep}{RST}", "")

    # ── строка уровня ──
    level_label  = f"  УРОВЕНЬ {idx}/{total_levels}"
    name_padded  = f"  {name}"
    padding      = max(0, 62 - len(level_label) - len(name_padded))
    instant(f"{C}{level_label}{RST}{'  '}{Y}{name}{RST}")

    # ── нижний разделитель ──
    instant(f"  {DIM}{sep}{RST}", "")
    print()

    # ── описание задания ──
    if desc:
        for line in desc.split('\n'):
            fade_in_line(f"  {line}", W, steps=4, total_time=0.10)
        print()

    # ── зашифрованные данные в рамке ──
    if encoded:
        box_w = 54
        inner = f"  {encoded}"
        pad   = max(0, box_w - len(inner) - 2)
        instant(f"  ┌{'─' * box_w}┐", Y)
        instant(f"  │{inner}{' ' * pad} │", Y)
        instant(f"  └{'─' * box_w}┘", Y)
        print()

    # ── подсказка о командах ──
    instant(f"  {DIM}[ hint / подсказка ]  [ exit — вернуться к уровню ]{RST}", "")
    print()

# ── переход между уровнями ────────────────────────────────────────────────────

def level_transition(stage_idx):
    """Плавный переход: короткий matrix-дождь + горизонтальная черта."""
    if stage_idx < len(STAGES) - 1:
        print()
        matrix_rain(0.35)
        instant(f"  {DIM}{'═' * 58}{RST}", "")
        print()

# ── главная функция ───────────────────────────────────────────────────────────

def main():
    friend_name = ""
    attempts_total = 0

    import signal
    def handle_exit(sig, frame):
        bsod()
        clear()
        boot_sequence()
        show_mask()
        show_logo()

    signal.signal(signal.SIGINT, handle_exit)

    boot_sequence()
    clear()
    show_mask()
    show_logo()

    for stage_idx, (stype, name, desc, encoded, answer, hint) in enumerate(STAGES):
        stage_attempts = 0

        show_stage_header(stage_idx, stype, name, desc, encoded)
        progress_bar(stage_idx, len(STAGES) - 1, animated=(stage_idx > 0))
        print()

        prompt = get_prompt(stage_idx)

        while True:
            try:
                sys.stdout.write(G + f"  {prompt} " + RST)
                sys.stdout.flush()
                user_input = input().strip().lower()
            except EOFError:
                break

            if user_input in ("hint", "help", "подсказка", "хинт"):
                print()
                instant(f"  {'─' * 50}", Y)
                instant(f"  💡  {hint}", Y)
                instant(f"  {'─' * 50}", Y)
                print()
                continue

            if user_input in ("exit", "quit", "close", "выход"):
                bsod()
                clear()
                show_mask()
                show_logo()
                show_stage_header(stage_idx, stype, name, desc, encoded)
                progress_bar(stage_idx, len(STAGES) - 1, animated=False)
                print()
                continue

            attempts_total += 1
            stage_attempts += 1

            # Финальный уровень — любое имя
            if stype == "name":
                friend_name = user_input.capitalize()
                print()
                fade_in_line(f"  ✓  Идентификация успешна. Добро пожаловать, {friend_name}.", G)
                time.sleep(0.5)
                show_win(friend_name)
                instant(f"\n  {DIM}Всего попыток за квест: {attempts_total}{RST}", "")
                print()
                return

            if user_input == answer:
                print()
                fade_in_line(f"  ✓  ВЕРНО!  Уровень {stage_idx} пройден.", BG)
                time.sleep(0.25)
                level_transition(stage_idx)
                break
            else:
                print()
                instant(f"  ✗  Неверно. Попробуй ещё.  (попытка {stage_attempts})", R)
                if stage_attempts == 2:
                    instant(f"  {DIM}→  Введи 'hint' для подсказки.{RST}", "")
                print()

if __name__ == "__main__":
    main()
