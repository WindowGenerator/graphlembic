class Commands:
    """Define library API"""
    def upgrade(self) -> None:
        ...
    
    def downgrade(self) -> None:
        ...
    
    def head(self) -> None:
        ...
    
    def current(self) -> None:
        ...
    
    def history(self) -> None:
        ...
    
