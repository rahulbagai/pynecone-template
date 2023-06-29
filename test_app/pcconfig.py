import pynecone as pc

class TestappConfig(pc.Config):
    pass

config = TestappConfig(
    app_name="test_app",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)