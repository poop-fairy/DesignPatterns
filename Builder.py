"""
Challange:
Implement a configuration manager for a game using the Builder Pattern.
The game has various settings, including graphics quality, sound volumes,
and control preferences
"""


class GraphicSettings:
    def __init__(self):
        self._resolution = None  # 1920x1080, 2560x1440, or 3840x2160.
        self._graphics_quality = None  # Low, Medium, High, Ultra.
        self._texture_quality = None  # Low, Medium, High, Ultra.
        self._shadow_quality = None  # Low, Medium, High.


class AudioPreferences:
    def __init__(self):
        self._volume_controls = None  # Percentage sliders (0-100)
        self._audio_output = None  # Speakers, Headphones.
        self._subtitles = None  # On, Off.


class ControlPreferences:
    def __init__(self):
        self._key_bindings = None  # Customizable key mappings.
        self._mouse_sensitivity = None  # Numerical sensitivity value.


class GraphicSettingsBuilder:
    def __init__(self):
        self._graphic_settings = GraphicSettings()

    def set_resolution(self, resolution):
        self._graphic_settings._resolution = resolution
        return self

    def set_graphics_quality(self, graphics_quality):
        self._graphic_settings._graphics_quality = graphics_quality
        return self

    def set_texture_quality(self, texture_quality):
        self._graphic_settings._texture_quality = texture_quality
        return self

    def set_shadow_quality(self, shadow_quality):
        self._graphic_settings._shadow_quality = shadow_quality
        return self

    def build(self):
        return self._graphic_settings


class AudioPreferencesBuilder:
    def __init__(self):
        self._audio_preferences = AudioPreferences()

    def set_volume_controls(self, volume_controls):
        self._audio_preferences._volume_controls = volume_controls
        return self

    def set_audio_output(self, audio_output):
        self._audio_preferences._audio_output = audio_output
        return self

    def set_subtitles(self, subtitles):
        self._audio_preferences._subtitles = subtitles
        return self

    def build(self):
        return self._audio_preferences


class ControlPreferencesBuilder:
    def __init__(self):
        self._control_preferences = ControlPreferences()

    def set_key_bindings(self, key_bindings):
        self._control_preferences._key_bindings = key_bindings
        return self

    def set_mouse_sensitivity(self, mouse_sensitivity):
        self._control_preferences._mouse_sensitivity = mouse_sensitivity
        return self

    def build(self):
        return self._control_preferences


class PreferencesDirector:
    def __init__(
        self,
        graphic_builder=GraphicSettingsBuilder(),
        audio_builder=AudioPreferencesBuilder(),
        control_builder=ControlPreferencesBuilder(),
    ):
        self._graphic_builder = graphic_builder
        self._audio_builder = audio_builder
        self._control_builder = control_builder

    def construct_preferences(
        self, graphic_settings, audio_preferences, control_preferences
    ):
        graphic_prefs = (
            self._graphic_builder.set_resolution(graphic_settings["resolution"])
            .set_graphics_quality(graphic_settings["graphics_quality"])
            .set_texture_quality(graphic_settings["texture_quality"])
            .set_shadow_quality(graphic_settings["shadow_quality"])
            .build()
        )

        audio_prefs = (
            self._audio_builder.set_volume_controls(
                audio_preferences["volume_controls"]
            )
            .set_audio_output(audio_preferences["audio_output"])
            .set_subtitles(audio_preferences["subtitles"])
            .build()
        )

        control_prefs = (
            self._control_builder.set_key_bindings(control_preferences["key_bindings"])
            .set_mouse_sensitivity(control_preferences["mouse_sensitivity"])
            .build()
        )

        return graphic_prefs, audio_prefs, control_prefs


graphic_settings = {
    "resolution": "1920x1080",
    "graphics_quality": "High",
    "texture_quality": "Ultra",
    "shadow_quality": "Medium",
}

audio_preferences = {
    "volume_controls": 80,
    "audio_output": "Speakers",
    "subtitles": "On",
}

control_preferences = {
    "key_bindings": {"move_forward": "W", "jump": "Space"},
    "mouse_sensitivity": 0.8,
}

director = PreferencesDirector()
graphic_prefs, audio_prefs, control_prefs = director.construct_preferences(
    graphic_settings, audio_preferences, control_preferences
)

print(graphic_settings, audio_preferences, control_preferences)
