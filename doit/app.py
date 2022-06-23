from textual.app import App
from textual.widgets import Placeholder
from rich.console import RenderableType
from textual.widget import Widget
from textual.widgets import Header

class App(App):

    async def on_load(self) -> None:
        await self.bind("q", "quit", "Quit")

    async def on_mount(self) -> None:
        await self.view.dock(Placeholder(), edge="left", size=40)
        await self.view.dock(Placeholder(), edge="top")

App.run(log="textual.log")
