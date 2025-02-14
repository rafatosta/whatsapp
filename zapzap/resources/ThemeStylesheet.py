

class ThemeStylesheet:

    # Componentes separados como strings
    PUSHBUTTON = {
        "light": """
            QPushButton {
                background-color: #F5F7F9;
                color: #202C33;
                border: 1px solid #D0D4D8;
                padding: 5px 10px;
                font-size: 14px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #E9ECEF;
                border: 1px solid #B0B6BB;
            }
            QPushButton:pressed {
                background-color: #DDE2E6;
                border: 1px solid #A0A6AB;
                color: #161E23;
            }
            QPushButton:disabled {
                background-color: #F0F2F5;
                color: #A6AEB6;
                border: 1px solid #D0D4D8;
            }
        """,
        "dark": """
            QPushButton {
                background-color: #364147;
                color: #E1E1E1;
                border: 1px solid #1c272d;
                padding: 5px 10px;
                font-size: 14px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #1c272d;
                border: 1px solid #6A6A6A;
            }
            QPushButton:pressed {
                background-color: #192328;
                border: 1px solid #1c272d;
                color: #FFFFFF;
            }
            QPushButton:disabled {
                background-color: #1c272d;
                color: #364147;
                border: 1px solid #1c272d;
            }
    """
    }

    TOOLTIP = {
        "light": """
            QToolTip {
                background-color: #ffffff; /* Fundo branco */
                color: #000000; /* Texto preto */
                border: 1px solid #cccccc; /* Borda cinza clara */
                border-radius: 4px; /* Bordas arredondadas */
                padding: 4px; /* Espaçamento interno */
                font-size: 12px; /* Tamanho da fonte */
            }
            """,
        "dark": """
            QToolTip {
                background-color: #333333; /* Fundo cinza escuro */
                color: #ffffff; /* Texto branco */
                border: 1px solid #aaaaaa; /* Borda cinza média */
                border-radius: 4px; /* Bordas arredondadas */
                padding: 4px; /* Espaçamento interno */
                font-size: 12px; /* Tamanho da fonte */
            }
        """
    }

    CHECKABLE_PUSHBUTTON = {
        "light": """
            QPushButton:checked {
                background-color: #00BD95;
                color: #FFFFFF;
                border: 1px solid #009C7A;
            }
            QPushButton:checked:hover {
                background-color: #009C7A;
                border: 1px solid #007F63;
            }
            QPushButton:checked:pressed {
                background-color: #007F63;
                border: 1px solid #006C55;
            }
        """,
        "dark": """
            QPushButton:checked {
                background-color: #00BD95;
                color: #FFFFFF;
                border: 1px solid #009C7A;
            }
            QPushButton:checked:hover {
                background-color: #009C7A;
                border: 1px solid #007F63;
            }
            QPushButton:checked:pressed {
                background-color: #007F63;
                border: 1px solid #006C55;
            }
        """
    }

    SIDEBAR = {
        "light": """
            QWidget#sidebar {
                background-color: #f0f2f5;
                border-right: 1px solid #c0c1c4;
                padding: 10px;
            }
        """,
        "dark": """
            QWidget#sidebar {
                background-color: #202C33;
                border-right: 1px solid #364147;
                padding: 10px;
            }
        """
    }

    SIDEBAR_SETTINGS_BUTTONS = {
        "light": """
            QWidget#menu_layout QPushButton {
                background-color: #f0f2f5;
                color: #202c33;
                border: none;
                padding: 10px 15px;
                text-align: left;
                font-size: 14px;
                border-radius: 4px;
                border-left: 3px solid #a8a9ab;
            }
            QWidget#menu_layout QPushButton:hover {
                background-color: #f9f9fb;
                border-left: 4px solid #00BD95;
            }
            QWidget#menu_layout QPushButton:pressed {
                background-color: #d8d9dc;
                color: #202c33;
            }
            QWidget#menu_layout QPushButton:disabled {
                background-color: #d8d9dc;
                border-left: 4px solid #00BD95;
            }
        """,
        "dark": """
            QWidget#menu_layout QPushButton {
                background-color: #202C33;
                color: #E1E1E1;
                border: none;
                padding: 10px 15px;
                text-align: left;
                font-size: 14px;
                border-radius: 4px;
                border-left: 3px solid #364147;
            }
            QWidget#menu_layout QPushButton:hover {
                background-color: #364147;
                border-left: 4px solid #00BD95;
            }
            QWidget#menu_layout QPushButton:pressed {
                background-color: #1c272d;
                color: #FFFFFF;
            }
            QWidget#menu_layout QPushButton:disabled {
                background-color: #1c272d;
                border-left: 4px solid #00BD95;
            }
        """
    }

    LABELS = {
        "light": """
            QLabel {
                color: #202C33; /* Cor do texto */
                font-size: 14px; /* Tamanho do texto */
                background-color: transparent; /* Fundo transparente */
                padding: 2px 0; /* Espaçamento interno */
            }

            /* Estilo para QLabel com texto de destaque */
            QLabel[role="highlight"] {
                color: #00BD95; /* Texto destacado em verde */
                font-weight: bold; /* Negrito para destaque */
            }

            /* Estilo para QLabel desativado */
            QLabel:disabled {
                color: #A6AEB6; /* Texto desbotado */
            }
            QWidget#menu_layout QLabel {
                color: #78797a;
                padding: 2px 0;
                margin-top: 8px;
            }
        """,
        "dark": """
            QLabel {
                color: #E1E1E1; /* Cor do texto */
                font-size: 14px; /* Tamanho do texto */
                background-color: transparent; /* Fundo transparente */
                padding: 2px 0; /* Espaçamento interno */
            }

            /* Estilo para QLabel com texto de destaque */
            QLabel[role="highlight"] {
                color: #00BD95; /* Texto destacado em verde */
                font-weight: bold; /* Negrito para destaque */
            }

            /* Estilo para QLabel desativado */
            QLabel:disabled {
                color: #A6AEB6; /* Texto desbotado */
            }
            QWidget#menu_layout QLabel {
                color: #A6AEB6;
                padding: 2px 0;
                margin-top: 8px;
            }
        """
    }

    SIDEBAR_BROWSER_BUTTONS = {
        "light": """
            QWidget#settings_buttons_layout QPushButton {
                background-color: #f0f2f5;
                border: none;
                border-radius: none;
                qproperty-flat: true;
            }
            QWidget#settings_buttons_layout QPushButton:hover {
                border-radius: 2px;
                border-left: 3px solid #a8a9ab;
            }
            QWidget#settings_buttons_layout QPushButton:pressed {
                background-color: rgba(225, 225, 225, 0.3);
                border-radius: 2px;
                height: 30px;
                border-left: 3px solid #00BD95;
            }
        """,
        "dark": """
            QWidget#settings_buttons_layout QPushButton {
                background-color: #202C33;
                border: none;
                border-radius: none;
                qproperty-flat: true;
            }
            QWidget#settings_buttons_layout QPushButton:hover {
                border-radius: 2px;
                border-left: 3px solid #364147;
            }
            QWidget#settings_buttons_layout QPushButton:pressed {
                background-color: rgba(60, 60, 60, 0.3);
                border-radius: 2px;
                height: 30px;
                border-left: 3px solid #00BD95;
            }
        """
    }

    FRAMES = {
        "light": """
            QFrame[frameShape="4"] {
                border: none;
                border-bottom: 1px solid rgba(192, 191, 188, 0.2);
            }
            QFrame[frameShape="5"] {
                border: none;
                border-left: 1px solid rgba(192, 191, 188, 0.2);
            }
            #frame_accounts #frame_carduser {
                background-color: #F5F7F9; /* Fundo claro */
                border: 1px solid #D0D4D8; /* Borda suave */
                border-radius: 6px; /* Bordas arredondadas */
                padding: 10px; /* Espaçamento interno */
            }
        """,
        "dark": """
            QFrame[frameShape="4"] {
                border: none;
                border-bottom: 1px solid #626b70;
            }
            QFrame[frameShape="5"] {
                border: none;
                border-left: 1px solid #626b70;
            }
            #frame_accounts #frame_carduser {
                background-color: #364147; /* Fundo escuro */
                border: 1px solid #364147; /* Borda suave */
                border-radius: 6px; /* Bordas arredondadas */
                padding: 10px; /* Espaçamento interno */
            }
        """
    }

    SPECIAL_BUTTONS = {
        "light": """
            #btn_back {
                color: rgb(61, 56, 70);
                text-align: left;
            }
            #btn_back:hover {
                color: rgb(98, 160, 234);
            }
            #btn_quit {
                color: rgb(61, 56, 70);
                text-align: left;
            }
            #btn_quit:hover {
                color: rgb(224, 27, 36);
            }
        """,
        "dark": """
            #btn_back {
                color: rgb(191, 191, 191);
                text-align: left;
            }
            #btn_back:hover {
                color: rgb(98, 160, 234);
            }
            #btn_quit {
                color: rgb(191, 191, 191);
                text-align: left;
            }
            #btn_quit:hover {
                color: rgb(224, 27, 36);
            }
        """
    }

    COMBOBOX = {
        "light": """
            QComboBox {
                background-color: #F5F7F9;
                color: #202C33;
                border: 1px solid #D0D4D8;
                padding: 5px 10px;
                font-size: 14px;
                border-radius: 6px;
                combobox-popup: 0;
            }
            QComboBox:hover {
                background-color: #E9ECEF;
                border: 1px solid #B0B6BB;
            }
            QComboBox:pressed {
                background-color: #DDE2E6;
                border: 1px solid #A0A6AB;
            }
            QComboBox:disabled {
                background-color: #F0F2F5;
                color: #A6AEB6;
                border: 1px solid #D0D4D8;
            }
            QComboBox::drop-down {
                border: none;
                background-color: transparent;
                width: 30px;
            }
            QComboBox::down-arrow {
                width: 12px;
                height: 12px;
            }
        """,
        "dark": """
            QComboBox {
                background-color: #202C33;
                color: #E1E1E1;
                border: 1px solid #364147;
                padding: 5px 10px;
                font-size: 14px;
                border-radius: 6px;
                combobox-popup: 0;
            }
            QComboBox:hover {
                background-color: #1c272d;
                border: 1px solid #364147;
            }
            QComboBox:pressed {
                background-color: #364147;
                border: 1px solid #A0A6AB;
            }
            QComboBox:disabled {
                background-color: #202C33;
                color: #A6AEB6;
                border: 1px solid #364147;
            }
            QComboBox::drop-down {
                border: none;
                background-color: transparent;
                width: 30px;
            }
            QComboBox::down-arrow {
                width: 12px;
                height: 12px;
            }
            QComboBox QAbstractItemView {
                background-color: #161e23;
                selection-background-color: #008069;
                padding: 6px 12px;
                margin: 2px 0;
                border-radius: 4px;
            }   
        """
    }

    LINE_EDIT = {
        "light": """
            QLineEdit {
                background-color: #F5F7F9;
                color: #202C33;
                border: 1px solid #D0D4D8;
                padding: 5px 10px;
                font-size: 14px;
                border-radius: 6px;
            }
            QLineEdit:hover {
                background-color: #E9ECEF;
                border: 1px solid #B0B6BB;
            }
            QLineEdit:focus {
                background-color: #FFFFFF;
                border: 1px solid #00BD95;
                outline: none;
            }
            QLineEdit:disabled {
                background-color: #F0F2F5;
                color: #A6AEB6;
                border: 1px solid #D0D4D8;
            }
        """,
        "dark": """
            QLineEdit {
                background-color: #202C33;
                color: #E1E1E1;
                border: 1px solid #364147;
                padding: 5px 10px;
                font-size: 14px;
                border-radius: 6px;
            }
            QLineEdit:hover {
                background-color: #1c272d;
                border: 1px solid #364147;
            }
            QLineEdit:focus {
                background-color: #1c272d;
                border: 1px solid #00BD95;
                outline: none;
            }
            QLineEdit:disabled {
                background-color: #202C33;
                color: #A6AEB6;
                border: 1px solid #364147;
            }
        """
    }

    MENU = {
        "light": """
            QMenu {
                background-color: #FFFFFF;
                border: 1px solid #D0D4D8;
                border-radius: 6px;
                padding: 5px;
                color: #202C33;
                font-size: 14px;
            }
            QMenu::item {
                background-color: transparent;
                padding: 6px 12px;
                margin: 2px 0;
                border-radius: 4px;
            }
            QMenu::item:selected {
                background-color: #E9ECEF;
                color: #202C33;
            }
            QMenu::item:pressed {
                background-color: #DDE2E6;
                color: #161E23;
            }
            QMenu:disabled {
                background-color: #F5F7F9;
                border: 1px solid #D0D4D8;
                color: #A6AEB6;
            }
            QMenu::item:disabled {
                color: #A6AEB6;
                background-color: transparent;
            }
            QMenu::indicator {
                width: 10px;
                height: 10px;
                border: 2px solid #D0D4D8;
                border-radius: 4px;
                background-color: #FFFFFF;
            }
            QMenu::indicator:checked {
                background-color: #00BD95;
                border: 2px solid #00BD95;
            }
            QMenu::indicator:unchecked {
                background-color: #F5F7F9;
                border: 2px solid #D0D4D8;
            }
            QMenu::right-arrow {
                padding-left: 8px;
            }
        """,
        "dark": """
            QMenu {
                background-color: #2E2E2E;
                border: 1px solid #444444;
                border-radius: 6px;
                padding: 5px;
                color: #FFFFFF;
                font-size: 14px;
            }
            QMenu::item {
                background-color: transparent;
                padding: 6px 12px;
                margin: 2px 0;
                border-radius: 4px;
            }
            QMenu::item:selected {
                background-color: #444444;
                color: #FFFFFF;
            }
            QMenu::item:pressed {
                background-color: #666666;
                color: #FFFFFF;
            }
            QMenu:disabled {
                background-color: #333333;
                border: 1px solid #555555;
                color: #777777;
            }
            QMenu::item:disabled {
                color: #777777;
                background-color: transparent;
            }
            QMenu::indicator {
                width: 10px;
                height: 10px;
                border: 2px solid #555555;
                border-radius: 4px;
                background-color: #333333;
            }
            QMenu::indicator:checked {
                background-color: #00BD95;
                border: 2px solid #00BD95;
            }
            QMenu::indicator:unchecked {
                background-color: #444444;
                border: 2px solid #555555;
            }
            QMenu::right-arrow {
                padding-left: 8px;
            }
            """
    }

    TABLE = {
        "light": """
            QTableWidget {
                background-color: #F5F7F9;
                color: #202C33;
                border: 1px solid #D0D4D8;
                gridline-color: #D0D4D8;
                font-size: 14px;
                border-radius: 6px;
            }
            QHeaderView::section {
                background-color: #E9ECEF;
                color: #202C33;
                padding: 5px;
                border: 1px solid #D0D4D8;
                font-weight: bold;
            }
            QHeaderView::section:hover {
                background-color: #DDE2E6;
                border: 1px solid #B0B6BB;
            }
            QTableWidget::item:selected {
                background-color: #00BD95;
                color: #FFFFFF;
            }
            QTableWidget::item {
                background-color: #FFFFFF;
            }
            QTableWidget::item:nth-child(even) {
                background-color: #F0F2F5;
            }
            QScrollBar:vertical {
                background: #E9ECEF;
                width: 10px;
                margin: 0px 0px 0px 0px;
                border: none;
            }
            QScrollBar::handle:vertical {
                background: #B0B6BB;
                min-height: 20px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical:hover {
                background: #00BD95;
            }
            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                background: none;
                border: none;
            }
            QTableWidget::item:disabled {
                background-color: #F0F2F5;
                color: #A6AEB6;
            }
        """,
        "dark": """
            QTableWidget {
                background-color: #2E2E2E;
                color: #E1E1E1;
                border: 1px solid #444444;
                gridline-color: #555555;
                font-size: 14px;
                border-radius: 6px;
            }
            QHeaderView::section {
                background-color: #444444;
                color: #E1E1E1;
                padding: 5px;
                border: 1px solid #555555;
                font-weight: bold;
            }
            QHeaderView::section:hover {
                background-color: #555555;
                border: 1px solid #666666;
            }
            QTableWidget::item:selected {
                background-color: #00BD95;
                color: #FFFFFF;
            }
            QTableWidget::item {
                background-color: #333333;
            }
            QTableWidget::item:nth-child(even) {
                background-color: #444444;
            }
            QScrollBar:vertical {
                background: #444444;
                width: 10px;
                margin: 0px 0px 0px 0px;
                border: none;
            }
            QScrollBar::handle:vertical {
                background: #666666;
                min-height: 20px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical:hover {
                background: #00BD95;
            }
            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                background: none;
                border: none;
            }
            QTableWidget::item:disabled {
                background-color: #444444;
                color: #777777;
            }
            """
    }

    GROUP_BOX = {
        "light": """
            QGroupBox {
                background-color: #F5F7F9;
                color: #202C33;
                border: 1px solid #D0D4D8;
                border-radius: 6px;
                margin-top: 20px;
                padding: 10px;
            }
            QGroupBox::title {
                background-color: transparent;
                color: #202C33;
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 5px;
                font-weight: bold;
                font-size: 14px;
            }
            QGroupBox:disabled {
                background-color: #F0F2F5;
                color: #A6AEB6;
                border: 1px solid #D0D4D8;
            }
            QGroupBox:disabled::title {
                color: #A6AEB6;
            }

            QGroupBox:checked::title {
                color: #2DBA2D;
            }
            QGroupBox::indicator {
                width: 10px;
                height: 10px;
                border: 2px solid #D0D4D8;
                border-radius: 4px;
                background-color: #FFFFFF;
            }
            QGroupBox::indicator:checked {
                background-color: #00BD95;
                border: 2px solid #00BD95;
            }
            QGroupBox::indicator:unchecked {
                background-color: #F5F7F9;
                border: 2px solid #D0D4D8;
            }
        """,
        "dark": """
            QGroupBox {
                background-color: #364147;
                color: #E1E1E1;
                border: 1px solid #444444;
                border-radius: 6px;
                margin-top: 20px;
                padding: 10px;
            }
            QGroupBox::title {
                background-color: transparent;
                color: #E1E1E1;
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 5px;
                font-weight: bold;
                font-size: 14px;
            }
            QGroupBox:disabled {
                background-color: #333333;
                color: #777777;
                border: 1px solid #555555;
            }
            QGroupBox:disabled::title {
                color: #777777;
            }
            QGroupBox:checked::title {
                color: #1ABC9C;
            }
            QGroupBox::indicator {
                width: 10px;
                height: 10px;
                border: 2px solid #555555;
                border-radius: 4px;
                background-color: #444444;
            }
            QGroupBox::indicator:checked {
                background-color: #1ABC9C;
                border: 2px solid #1ABC9C;
            }
            QGroupBox::indicator:unchecked {
                background-color: #2D3E44;
                border: 2px solid #555555;
            }
        """
    }

    CHECK_BOX = {
        "light": """
            QCheckBox {
                color: #202C33;
                font-size: 14px;
                padding: 5px 0;
            }
            QCheckBox::indicator {
                width: 10px;
                height: 10px;
                border: 2px solid #D0D4D8;
                border-radius: 4px;
                background-color: #FFFFFF;
            }
            QCheckBox::indicator:checked {
                background-color: #00BD95;
                border: 2px solid #00BD95;
            }
            QCheckBox::indicator:unchecked {
                background-color: #F5F7F9;
                border: 2px solid #D0D4D8;
            }
            QCheckBox:hover {
                color: #00BD95;
            }
            QCheckBox:disabled {
                color: #A6AEB6;
            }
        """,
        "dark": """
            QCheckBox {
                color: #E1E1E1;
                font-size: 14px;
                padding: 5px 0;
            }
            QCheckBox::indicator {
                width: 10px;
                height: 10px;
                border: 2px solid #555555;
                border-radius: 4px;
                background-color: #333333;
            }
            QCheckBox::indicator:checked {
                background-color: #00BD95;
                border: 2px solid #00BD95;
            }
            QCheckBox::indicator:unchecked {
                background-color: #444444;
                border: 2px solid #555555;
            }
            QCheckBox:hover {
                color: #00BD95;
            }
            QCheckBox:disabled {
                color: #777777;
            }
        """
    }

    RADIO_BUTTON = {
        "light": """
            QRadioButton {
                color: #202C33;
                font-size: 14px;
                padding: 5px 0;
            }
            QRadioButton::indicator {
                width: 10px;
                height: 10px;
                border: 2px solid #D0D4D8;
                border-radius: 6px;
                background-color: #FFFFFF;
            }
            QRadioButton::indicator:checked {
                background-color: #00BD95;
                border: 2px solid #00BD95;
            }
            QRadioButton::indicator:unchecked {
                background-color: #F5F7F9;
                border: 2px solid #D0D4D8;
            }
            QRadioButton:disabled {
                color: #A6AEB6;
            }
            QRadioButton::indicator:disabled {
                background-color: #F0F2F5;
                border: 2px solid #D0D4D8;
            }
        """,
        "dark": """
            QRadioButton {
                color: #E1E1E1;
                font-size: 14px;
                padding: 5px 0;
            }
            QRadioButton::indicator {
                width: 10px;
                height: 10px;
                border: 2px solid #555555;
                border-radius: 6px;
                background-color: #333333;
            }
            QRadioButton::indicator:checked {
                background-color: #00BD95;
                border: 2px solid #00BD95;
            }
            QRadioButton::indicator:unchecked {
                background-color: #444444;
                border: 2px solid #555555;
            }
            QRadioButton:disabled {
                color: #777777;
            }
            QRadioButton::indicator:disabled {
                background-color: #444444;
                border: 2px solid #555555;
            }
        """
    }

    @staticmethod
    def get_stylesheet(theme) -> str:
        components = [
            ThemeStylesheet.PUSHBUTTON[theme],
            ThemeStylesheet.CHECKABLE_PUSHBUTTON[theme],
            ThemeStylesheet.SIDEBAR[theme],
            ThemeStylesheet.SIDEBAR_SETTINGS_BUTTONS[theme],
            ThemeStylesheet.LABELS[theme],
            ThemeStylesheet.SIDEBAR_BROWSER_BUTTONS[theme],
            ThemeStylesheet.FRAMES[theme],
            ThemeStylesheet.SPECIAL_BUTTONS[theme],
            ThemeStylesheet.COMBOBOX[theme],
            ThemeStylesheet.LINE_EDIT[theme],
            ThemeStylesheet.MENU[theme],
            ThemeStylesheet.TABLE[theme],
            ThemeStylesheet.GROUP_BOX[theme],
            ThemeStylesheet.CHECK_BOX[theme],
            ThemeStylesheet.RADIO_BUTTON[theme],
            ThemeStylesheet.TOOLTIP[theme]
        ]
        return "\n".join(components)
