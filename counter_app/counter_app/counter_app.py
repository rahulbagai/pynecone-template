import pynecone as pc

class State(pc.State):
    count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

def index():
    return pc.hstack(
        pc.button("-", on_click=State.decrement, bg="red"),
        pc.heading(State.count),
        pc.button("+", on_click=State.increment, bg="green")
    )

app = pc.App(state=State)
app.add_page(index, title="Counter")
app.compile()