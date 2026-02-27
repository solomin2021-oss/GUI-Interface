import customtkinter as ctk
from datetime import datetime
import random
from PIL import Image, ImageTk
import math

# Настройка темы
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ModernSmartHomeApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("🏠 Умный дом - Современная система управления")
        self.root.geometry("1200x700")
        
        # Переменные состояния
        self.lights_state = {
            "Гостиная": False, "Спальня": False, 
            "Кухня": False, "Ванная": False, "Кабинет": False
        }
        self.temperature = 22.5
        self.humidity = 45
        self.security_armed = False
        self.energy_consumption = 350  # Вт
        
        # Цветовая схема
        self.colors = {
            'primary': "#1f6aa5",
            'secondary': "#2b2b2b",
            'success': "#2bb673",
            'warning': "#ffb347",
            'danger': "#e74c3c",
            'surface': "#242424",
            'text': "#ffffff"
        }
        
        self.setup_ui()
        
    def setup_ui(self):
        # Основной контейнер
        self.main_container = ctk.CTkFrame(self.root, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Верхняя панель
        self.create_header()
        
        # Основной контент
        self.create_content()
        
        # Нижняя панель
        self.create_footer()
        
    def create_header(self):
        header = ctk.CTkFrame(self.main_container, height=80, corner_radius=15)
        header.pack(fill="x", pady=(0, 20))
        header.pack_propagate(False)
        
        # Левая часть с логотипом
        left_frame = ctk.CTkFrame(header, fg_color="transparent")
        left_frame.pack(side="left", padx=20, pady=10)
        
        title = ctk.CTkLabel(
            left_frame, 
            text="🏠 SMART HOME", 
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color=self.colors['primary']
        )
        title.pack(side="left")
        
        # Статус системы
        status_frame = ctk.CTkFrame(header, fg_color="transparent")
        status_frame.pack(side="right", padx=20)
        
        self.status_indicator = ctk.CTkLabel(
            status_frame,
            text="●",
            font=ctk.CTkFont(size=20),
            text_color=self.colors['success']
        )
        self.status_indicator.pack(side="left", padx=(0, 5))
        
        self.time_label = ctk.CTkLabel(
            status_frame,
            text="",
            font=ctk.CTkFont(size=16)
        )
        self.time_label.pack(side="left")
        
    def create_content(self):
        content = ctk.CTkFrame(self.main_container, fg_color="transparent")
        content.pack(fill="both", expand=True)
        
        # Левая боковая панель с навигацией
        self.create_sidebar(content)
        
        # Правая основная область с вкладками
        self.create_main_area(content)
        
    def create_sidebar(self, parent):
        sidebar = ctk.CTkFrame(parent, width=200, corner_radius=15)
        sidebar.pack(side="left", fill="y", padx=(0, 20))
        sidebar.pack_propagate(False)
        
        # Аватар/профиль
        profile_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        profile_frame.pack(pady=20)
        
        avatar = ctk.CTkLabel(
            profile_frame,
            text="👤",
            font=ctk.CTkFont(size=48)
        )
        avatar.pack()
        
        ctk.CTkLabel(
            profile_frame,
            text="Владелец",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack()
        
        ctk.CTkLabel(
            profile_frame,
            text="Онлайн",
            font=ctk.CTkFont(size=12),
            text_color=self.colors['success']
        ).pack()
        
        # Навигационные кнопки
        nav_buttons = [
            ("🏠 Главная", self.show_dashboard),
            ("💡 Освещение", self.show_lights),
            ("🌡️ Климат", self.show_climate),
            ("🔒 Безопасность", self.show_security),
            ("📊 Энергия", self.show_energy),
            ("⚙️ Настройки", self.show_settings)
        ]
        
        for text, command in nav_buttons:
            btn = ctk.CTkButton(
                sidebar,
                text=text,
                command=command,
                fg_color="transparent",
                text_color=self.colors['text'],
                anchor="w",
                height=40,
                corner_radius=10,
                hover_color=self.colors['primary']
            )
            btn.pack(pady=2, padx=10, fill="x")
            
    def create_main_area(self, parent):
        self.main_area = ctk.CTkFrame(parent, corner_radius=15)
        self.main_area.pack(side="left", fill="both", expand=True)
        
        # Контейнер для контента
        self.content_frame = ctk.CTkFrame(self.main_area, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # По умолчанию показываем дашборд
        self.show_dashboard()
        
    def create_footer(self):
        footer = ctk.CTkFrame(self.main_container, height=50, corner_radius=10)
        footer.pack(fill="x", pady=(20, 0))
        footer.pack_propagate(False)
        
        # Статус сообщения
        self.status_label = ctk.CTkLabel(
            footer,
            text="✓ Система работает нормально",
            font=ctk.CTkFont(size=12)
        )
        self.status_label.pack(side="left", padx=20)
        
        # Быстрые действия
        actions_frame = ctk.CTkFrame(footer, fg_color="transparent")
        actions_frame.pack(side="right", padx=20)
        
        actions = ["🔔", "📱", "🎤"]
        for action in actions:
            ctk.CTkButton(
                actions_frame,
                text=action,
                width=30,
                height=30,
                corner_radius=15,
                fg_color="transparent",
                hover_color=self.colors['primary']
            ).pack(side="left", padx=2)
            
    def show_dashboard(self):
        self.clear_content()
        
        # Заголовок
        title = ctk.CTkLabel(
            self.content_frame,
            text="Панель управления",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(anchor="w", pady=(0, 20))
        
        # Статистика в карточках
        stats_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        stats_frame.pack(fill="x", pady=(0, 20))
        
        stats = [
            ("💡", "Активных устройств", "8", self.colors['primary']),
            ("🌡️", "Температура", f"{self.temperature}°C", self.colors['warning']),
            ("🔒", "Безопасность", "Активна" if self.security_armed else "Отключена", 
             self.colors['success'] if self.security_armed else self.colors['danger']),
            ("⚡", "Энергопотребление", f"{self.energy_consumption} Вт", self.colors['warning'])
        ]
        
        for i, (icon, label, value, color) in enumerate(stats):
            card = ctk.CTkFrame(stats_frame, fg_color=self.colors['surface'], corner_radius=15)
            card.grid(row=0, column=i, padx=10, sticky="ew")
            stats_frame.grid_columnconfigure(i, weight=1)
            
            ctk.CTkLabel(card, text=icon, font=ctk.CTkFont(size=32)).pack(pady=(15,5))
            ctk.CTkLabel(card, text=label, font=ctk.CTkFont(size=12)).pack()
            ctk.CTkLabel(
                card, 
                text=value, 
                font=ctk.CTkFont(size=20, weight="bold"),
                text_color=color
            ).pack(pady=(5,15))
            
        # График энергопотребления
        chart_frame = ctk.CTkFrame(self.content_frame, fg_color=self.colors['surface'], corner_radius=15)
        chart_frame.pack(fill="both", expand=True, pady=(0, 20))
        
        ctk.CTkLabel(
            chart_frame,
            text="Энергопотребление за сегодня",
            font=ctk.CTkFont(size=16, weight="bold")
        ).pack(anchor="w", padx=20, pady=15)
        
        # Создаем простой график
        canvas_frame = ctk.CTkFrame(chart_frame, fg_color=self.colors['secondary'], corner_radius=10)
        canvas_frame.pack(fill="both", expand=True, padx=20, pady=(0,20))
        
        # Быстрые действия
        actions_title = ctk.CTkLabel(
            self.content_frame,
            text="Быстрые действия",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        actions_title.pack(anchor="w", pady=(10,10))
        
        actions_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        actions_frame.pack(fill="x")
        
        quick_actions = [
            ("🎬 Режим кино", self.cinema_mode, self.colors['primary']),
            ("😴 Ночной режим", self.night_mode, self.colors['secondary']),
            ("🏠 Все домa", self.everyone_home, self.colors['success']),
            ("🌅 Утро", self.morning_mode, self.colors['warning'])
        ]
        
        for i, (text, command, color) in enumerate(quick_actions):
            btn = ctk.CTkButton(
                actions_frame,
                text=text,
                command=command,
                fg_color=color,
                hover_color=color,
                height=50,
                corner_radius=10
            )
            btn.grid(row=0, column=i, padx=5, sticky="ew")
            actions_frame.grid_columnconfigure(i, weight=1)
            
    def show_lights(self):
        self.clear_content()
        
        title = ctk.CTkLabel(
            self.content_frame,
            text="Управление освещением",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(anchor="w", pady=(0, 20))
        
        # Сетка освещения
        lights_grid = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        lights_grid.pack(fill="both", expand=True)
        
        self.light_cards = {}
        rooms = list(self.lights_state.keys())
        
        for i, room in enumerate(rooms):
            row = i // 3
            col = i % 3
            
            card = ctk.CTkFrame(lights_grid, fg_color=self.colors['surface'], corner_radius=15)
            card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            
            lights_grid.grid_rowconfigure(row, weight=1)
            lights_grid.grid_columnconfigure(col, weight=1)
            
            # Иконка комнаты
            icons = {"Гостиная": "🛋️", "Спальня": "🛏️", "Кухня": "🍳", 
                    "Ванная": "🚿", "Кабинет": "💻"}
            
            ctk.CTkLabel(
                card,
                text=icons.get(room, "💡"),
                font=ctk.CTkFont(size=48)
            ).pack(pady=(20,10))
            
            ctk.CTkLabel(
                card,
                text=room,
                font=ctk.CTkFont(size=18, weight="bold")
            ).pack()
            
            # Статус
            status_label = ctk.CTkLabel(
                card,
                text="Выключено",
                font=ctk.CTkFont(size=12),
                text_color=self.colors['danger']
            )
            status_label.pack(pady=5)
            
            # Кнопка с иконкой
            btn = ctk.CTkButton(
                card,
                text="💡 Включить",
                command=lambda r=room, s=status_label: self.toggle_light(r, s),
                fg_color=self.colors['secondary'],
                hover_color=self.colors['primary'],
                height=40,
                corner_radius=10
            )
            btn.pack(pady=(10,20))
            
            self.light_cards[room] = {"button": btn, "status": status_label, "state": False}
            
    def show_climate(self):
        self.clear_content()
        
        title = ctk.CTkLabel(
            self.content_frame,
            text="Климат-контроль",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(anchor="w", pady=(0, 20))
        
        # Текущие показатели
        metrics_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        metrics_frame.pack(fill="x", pady=(0, 20))
        
        # Температура
        temp_card = ctk.CTkFrame(metrics_frame, fg_color=self.colors['surface'], corner_radius=15)
        temp_card.pack(side="left", fill="both", expand=True, padx=(0,10))
        
        ctk.CTkLabel(temp_card, text="🌡️", font=ctk.CTkFont(size=48)).pack(pady=(20,5))
        ctk.CTkLabel(temp_card, text="Температура", font=ctk.CTkFont(size=14)).pack()
        self.temp_display = ctk.CTkLabel(
            temp_card,
            text=f"{self.temperature}°C",
            font=ctk.CTkFont(size=32, weight="bold")
        )
        self.temp_display.pack(pady=(5,20))
        
        # Влажность
        humid_card = ctk.CTkFrame(metrics_frame, fg_color=self.colors['surface'], corner_radius=15)
        humid_card.pack(side="left", fill="both", expand=True, padx=(5,0))
        
        ctk.CTkLabel(humid_card, text="💧", font=ctk.CTkFont(size=48)).pack(pady=(20,5))
        ctk.CTkLabel(humid_card, text="Влажность", font=ctk.CTkFont(size=14)).pack()
        self.humid_display = ctk.CTkLabel(
            humid_card,
            text=f"{self.humidity}%",
            font=ctk.CTkFont(size=32, weight="bold")
        )
        self.humid_display.pack(pady=(5,20))
        
        # Управление
        control_frame = ctk.CTkFrame(self.content_frame, fg_color=self.colors['surface'], corner_radius=15)
        control_frame.pack(fill="both", expand=True)
        
        ctk.CTkLabel(
            control_frame,
            text="Настройка температуры",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=20)
        
        # Слайдер
        self.temp_slider = ctk.CTkSlider(
            control_frame,
            from_=16,
            to=30,
            number_of_steps=28,
            command=self.update_temperature,
            height=20,
            progress_color=self.colors['primary']
        )
        self.temp_slider.set(self.temperature)
        self.temp_slider.pack(fill="x", padx=40, pady=20)
        
        # Значения
        values_frame = ctk.CTkFrame(control_frame, fg_color="transparent")
        values_frame.pack(fill="x", padx=40)
        
        ctk.CTkLabel(values_frame, text="16°C", font=ctk.CTkFont(size=12)).pack(side="left")
        ctk.CTkLabel(values_frame, text="23°C", font=ctk.CTkFont(size=12)).pack(side="left", expand=True)
        ctk.CTkLabel(values_frame, text="30°C", font=ctk.CTkFont(size=12)).pack(side="right")
        
        # Кнопка симуляции
        ctk.CTkButton(
            control_frame,
            text="🌤️ Симулировать изменение погоды",
            command=self.simulate_weather,
            fg_color=self.colors['secondary'],
            hover_color=self.colors['primary'],
            height=50,
            corner_radius=10
        ).pack(pady=30)
        
    def show_security(self):
        self.clear_content()
        
        title = ctk.CTkLabel(
            self.content_frame,
            text="Безопасность",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(anchor="w", pady=(0, 20))
        
        # Статус системы
        status_card = ctk.CTkFrame(self.content_frame, fg_color=self.colors['surface'], corner_radius=15)
        status_card.pack(fill="x", pady=(0, 20))
        
        status_header = ctk.CTkFrame(status_card, fg_color="transparent")
        status_header.pack(fill="x", padx=20, pady=20)
        
        ctk.CTkLabel(
            status_header,
            text="🔒",
            font=ctk.CTkFont(size=48)
        ).pack(side="left", padx=(0,20))
        
        status_text_frame = ctk.CTkFrame(status_header, fg_color="transparent")
        status_text_frame.pack(side="left", fill="both", expand=True)
        
        ctk.CTkLabel(
            status_text_frame,
            text="Система безопасности",
            font=ctk.CTkFont(size=14)
        ).pack(anchor="w")
        
        self.security_status = ctk.CTkLabel(
            status_text_frame,
            text="Отключена",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=self.colors['danger']
        )
        self.security_status.pack(anchor="w")
        
        self.security_btn = ctk.CTkButton(
            status_header,
            text="🔒 Активировать",
            command=self.toggle_security,
            fg_color=self.colors['success'],
            hover_color=self.colors['success'],
            width=150,
            height=40,
            corner_radius=10
        )
        self.security_btn.pack(side="right")
        
        # Двери и окна
        sensors_frame = ctk.CTkFrame(self.content_frame, fg_color=self.colors['surface'], corner_radius=15)
        sensors_frame.pack(fill="both", expand=True)
        
        ctk.CTkLabel(
            sensors_frame,
            text="Датчики и сенсоры",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=20)
        
        # Список датчиков
        sensors = [
            ("Входная дверь", "Закрыта", self.colors['success']),
            ("Балконная дверь", "Закрыта", self.colors['success']),
            ("Окно гостиной", "Закрыто", self.colors['success']),
            ("Окно спальни", "Закрыто", self.colors['success']),
            ("Датчик движения", "Нет активности", self.colors['success']),
            ("Датчик дыма", "Норма", self.colors['success'])
        ]
        
        for sensor, state, color in sensors:
            sensor_row = ctk.CTkFrame(sensors_frame, fg_color="transparent")
            sensor_row.pack(fill="x", padx=20, pady=5)
            
            ctk.CTkLabel(
                sensor_row,
                text=sensor,
                font=ctk.CTkFont(size=14)
            ).pack(side="left")
            
            ctk.CTkLabel(
                sensor_row,
                text=state,
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color=color
            ).pack(side="right")
            
    def show_energy(self):
        self.clear_content()
        
        title = ctk.CTkLabel(
            self.content_frame,
            text="Энергопотребление",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(anchor="w", pady=(0, 20))
        
        # График потребления
        chart_card = ctk.CTkFrame(self.content_frame, fg_color=self.colors['surface'], corner_radius=15)
        chart_card.pack(fill="both", expand=True)
        
        ctk.CTkLabel(
            chart_card,
            text="Потребление электроэнергии",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=20)
        
        # Визуализация потребления
        canvas_frame = ctk.CTkFrame(chart_card, fg_color=self.colors['secondary'], corner_radius=10)
        canvas_frame.pack(fill="both", expand=True, padx=20, pady=(0,20))
        
        # Текущее потребление
        consumption_frame = ctk.CTkFrame(chart_card, fg_color="transparent")
        consumption_frame.pack(fill="x", padx=20, pady=20)
        
        ctk.CTkLabel(
            consumption_frame,
            text="Текущее потребление:",
            font=ctk.CTkFont(size=14)
        ).pack(side="left")
        
        ctk.CTkLabel(
            consumption_frame,
            text=f"{self.energy_consumption} Вт",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=self.colors['warning']
        ).pack(side="left", padx=(10,0))
        
    def show_settings(self):
        self.clear_content()
        
        title = ctk.CTkLabel(
            self.content_frame,
            text="Настройки",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(anchor="w", pady=(0, 20))
        
        # Настройки в виде списка
        settings_frame = ctk.CTkFrame(self.content_frame, fg_color=self.colors['surface'], corner_radius=15)
        settings_frame.pack(fill="both", expand=True)
        
        settings_options = [
            ("Тема оформления", "Темная", self.colors['primary']),
            ("Язык интерфейса", "Русский", self.colors['primary']),
            ("Уведомления", "Включены", self.colors['success']),
            ("Автоматизация", "Активна", self.colors['success']),
            ("Голосовое управление", "Отключено", self.colors['danger']),
            ("Геолокация", "Активна", self.colors['success'])
        ]
        
        for i, (setting, value, color) in enumerate(settings_options):
            setting_row = ctk.CTkFrame(settings_frame, fg_color="transparent")
            setting_row.pack(fill="x", padx=20, pady=10)
            
            ctk.CTkLabel(
                setting_row,
                text=setting,
                font=ctk.CTkFont(size=14)
            ).pack(side="left")
            
            ctk.CTkLabel(
                setting_row,
                text=value,
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color=color
            ).pack(side="right")
            
            if i < len(settings_options) - 1:
                separator = ctk.CTkFrame(settings_frame, height=1, fg_color=self.colors['secondary'])
                separator.pack(fill="x", padx=20)
                
    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
            
    def toggle_light(self, room, status_label):
        current_state = self.light_cards[room]["state"]
        self.light_cards[room]["state"] = not current_state
        
        if self.light_cards[room]["state"]:
            status_label.configure(text="Включено", text_color=self.colors['success'])
            self.light_cards[room]["button"].configure(text="💡 Выключить")
        else:
            status_label.configure(text="Выключено", text_color=self.colors['danger'])
            self.light_cards[room]["button"].configure(text="💡 Включить")
            
        self.update_status(f"Свет в {room} {'включен' if self.light_cards[room]['state'] else 'выключен'}")
        
    def update_temperature(self, value):
        self.temperature = value
        self.temp_display.configure(text=f"{value:.1f}°C")
        
    def simulate_weather(self):
        self.temperature += random.uniform(-0.5, 0.5)
        self.humidity += random.randint(-2, 2)
        
        self.temperature = max(16, min(30, self.temperature))
        self.humidity = max(20, min(80, self.humidity))
        
        self.temp_display.configure(text=f"{self.temperature:.1f}°C")
        self.humid_display.configure(text=f"{self.humidity}%")
        self.temp_slider.set(self.temperature)
        
        self.update_status("Показатели климата обновлены")
        
    def toggle_security(self):
        self.security_armed = not self.security_armed
        
        if self.security_armed:
            self.security_status.configure(text="Активна", text_color=self.colors['success'])
            self.security_btn.configure(text="🔓 Деактивировать", fg_color=self.colors['danger'])
            self.update_status("Охранная система активирована")
        else:
            self.security_status.configure(text="Отключена", text_color=self.colors['danger'])
            self.security_btn.configure(text="🔒 Активировать", fg_color=self.colors['success'])
            self.update_status("Охранная система деактивирована")
            
    def cinema_mode(self):
        for room in self.light_cards:
            if room != "Гостиная":
                self.light_cards[room]["state"] = False
                if "status" in self.light_cards[room]:
                    self.light_cards[room]["status"].configure(text="Выключено", text_color=self.colors['danger'])
        self.update_status("🎬 Активирован режим кино")
        
    def night_mode(self):
        for room in self.light_cards:
            self.light_cards[room]["state"] = False
            if "status" in self.light_cards[room]:
                self.light_cards[room]["status"].configure(text="Выключено", text_color=self.colors['danger'])
        self.security_armed = True
        self.update_status("😴 Активирован ночной режим")
        
    def everyone_home(self):
        if "Гостиная" in self.light_cards:
            self.light_cards["Гостиная"]["state"] = True
            if "status" in self.light_cards["Гостиная"]:
                self.light_cards["Гостиная"]["status"].configure(text="Включено", text_color=self.colors['success'])
        self.security_armed = False
        self.update_status("🏠 Все дома")
        
    def morning_mode(self):
        if "Кухня" in self.light_cards:
            self.light_cards["Кухня"]["state"] = True
            if "status" in self.light_cards["Кухня"]:
                self.light_cards["Кухня"]["status"].configure(text="Включено", text_color=self.colors['success'])
        self.update_status("🌅 Доброе утро!")
        
    def update_status(self, message):
        self.status_label.configure(text=f"✓ {message}")
        
    def run(self):
        self.update_time()
        self.root.mainloop()
        
    def update_time(self):
        current_time = datetime.now().strftime("%H:%M")
        current_date = datetime.now().strftime("%d.%m.%Y")
        self.time_label.configure(text=f"{current_date} {current_time}")
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    app = ModernSmartHomeApp()
    app.run()