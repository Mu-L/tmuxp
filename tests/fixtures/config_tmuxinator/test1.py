from .._util import loadfixture

tmuxinator_yaml = loadfixture("config_tmuxinator/test1.yaml")
tmuxinator_dict = {
    "windows": [
        {"editor": {"layout": "main-vertical", "panes": ["vim", "guard"]}},
        {"server": "bundle exec rails s"},
        {"logs": "tail -f logs/development.log"},
    ]
}

expected = {
    "session_name": None,
    "windows": [
        {"window_name": "editor", "layout": "main-vertical", "panes": ["vim", "guard"]},
        {"window_name": "server", "panes": ["bundle exec rails s"]},
        {"window_name": "logs", "panes": ["tail -f logs/development.log"]},
    ],
}
