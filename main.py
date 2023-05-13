import tcod
from actions import EscapeAction, MovementAction
from inputHandlers import EventHandler


def main() -> None:
    # TODO вынести задающие параметры в отдельные функции и файлы
    # задаём ширину, высоту
    screen_width = 80
    screen_height = 50

    # тречим позицию игрока
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    # подгружаем тайлсет, картинку с используемыми тайлами
    # TODO сделать свою
    tileset = tcod.tileset.load_tilesheet(
        "src/Md_curses_16x16.png", 16, 16, tcod.tileset.CHARMAP_CP437
    )
    # это дефолтный
    # tileset = tcod.tileset.load_tilesheet(
    #     "src/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    # )

    #
    event_handler = EventHandler()
    # создаём окно с параметрами
    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title="No Mads here... or not?",
            vsync=True
    ) as context:
        # создаём консоль с нужным размером, задаём порядок координат [x,y], по умолчанию [y,x]
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            root_console.print(x=player_x, y=player_y, string="\u263A")

            # отображаем написанное, аля update
            context.present(root_console)

            root_console.clear()

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue
                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy
                elif isinstance(action, EscapeAction):
                    raise SystemExit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
