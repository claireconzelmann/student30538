import seaborn as sns

# Import data from shared.py
from shared import df

from shiny import App, render, ui

page1 = ui.navset_card_underline(
    ui.nav_panel("Plot", ui.output_plot("hist")),
    ui.nav_panel("Table", ui.output_data_frame("data")),
    footer=ui.input_select(
        id = "var", 
        label = "Select variable", 
        choices = ["bill_length_mm", "body_mass_g"]
    ),
    title="Penguins data",
)

page2 = ui.navset_card_underline(
    ui.card("Plot", ui.output_plot("hist")),
    ui.nav_panel("Table", ui.output_data_frame("data")),
    footer=ui.input_select(
        id = "var", 
        label = "Select variable", 
        choices = ["bill_length_mm", "body_mass_g"]
    ),
    title="Penguins data",
)

app_ui = ui.page_navbar(
    ui.nav_spacer(),  
    ui.nav_panel("Page 1", page1),
    ui.nav_panel("Page 2", page2),
    title="Shiny navigation components",
)


def server(input, output, session):
    @render.plot
    def hist():
        p = sns.histplot(df, x=input.var(), facecolor="#007bc2", edgecolor="white")
        return p.set(xlabel=None)

    @render.data_frame
    def data():
        return df[["species", "island", input.var()]]


app = App(app_ui, server)
