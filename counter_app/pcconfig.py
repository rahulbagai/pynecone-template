import pynecone as pc

class CounterappConfig(pc.Config):
    pass

config = CounterappConfig(
    app_name="counter_app",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)