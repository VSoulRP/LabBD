from django import forms

CountryColumns = [
    ('confirmed', 'Confirmados'),
    ('deaths', 'Muertes'),
    ('recovered', 'Recuperados'),
    ('active', 'Activos'),
    ('new_cases', 'Nuevos Casos'),
    ('new_deaths', 'Nuevas Muertes'),
    ('new_recovered', 'Nuevos Recuperados'),
    ('deaths_per_100_cases', 'Muertes / Casos'),
    ('recovered_per_100_cases', 'Recuperadors / 100 Casos'),
    ('deaths_per_100_recovered', 'Muertes / 100 Recuperados'),
    ('confirmed_last_week', 'Confirmado ultima semana'),
    ('one_week_change', 'Cambio en una semana'),
    ('one_week_perc_increase', 'Incremento % en una semana'),
]

DayColumns = [
    ('confirmed', 'Confirmados'),
    ('deaths', 'Muertes'),
    ('recovered', 'Recuperados'),
    ('active', 'Activos'),
    ('new_cases', 'Nuevos Casos'),
    ('new_deaths', 'Nuevas Muertes'),
    ('new_recovered', 'Nuevos recuperados'),
    ('deaths_per_100_cases', 'Muertes / Casos'),
    ('recovered_per_100_cases', 'Muertos / 100 Casos'),
    ('deaths_per_100_recovered', 'Muertes / 100 Recuperados'),
    ('num_of_countries', 'Numero de Paises'),
]

OrderOptions = [
    ('', '----'),
    ('-', 'Desc'),
    ('+', 'Asc'),
]

SelectionOptionsDay = [
    ('', '--------------'),
    ('pk', 'Fecha'),
    ('column', 'Columna Escogida'),
]

SelectionOptionsCountry = [
    ('', '--------------'),
    ('pk', 'País'),
    ('column', 'Columna Escogida'),
]

class CountryForm(forms.Form):
    ColumnMenu = forms.ChoiceField(label='Menú Columnas', choices=CountryColumns)
    OrderSelection = forms.ChoiceField(label='Organizar por', choices=SelectionOptionsCountry, required=False)
    OrderMenu = forms.ChoiceField(label='Menú Orden', choices=OrderOptions, required=False)
    start = forms.IntegerField(label='Inicio', required=False)
    end = forms.IntegerField(label='Fin', required=False)


class DayForm(forms.Form):
    ColumnMenu = forms.ChoiceField(label='Menú Columnas', choices=DayColumns)
    OrderSelection = forms.ChoiceField(label='Organizar por', choices=SelectionOptionsDay, required=False)
    OrderMenu = forms.ChoiceField(label='Menú Orden', choices=OrderOptions, required=False)
    start = forms.IntegerField(label='Inicio', required=False)
    end = forms.IntegerField(label='Fin', required=False)
