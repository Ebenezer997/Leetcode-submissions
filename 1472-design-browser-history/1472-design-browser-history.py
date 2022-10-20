class BrowserHistory:
    

    def __init__(self, homepage: str):
        self.curPage = homepage # We keep track of the page we are currently on
        self.prevStack = [] # We keep track of the pages if we were to go back 
        self.forwardStack = [] # We keep track of the pages if we were to go forward

    def visit(self, url: str) -> None:      
        
        self.prevStack.append(self.curPage) # Step 1
        self.forwardStack = [] # Step 2
        self.curPage = url # Step 3
        

    def back(self, steps: int) -> str:
        
        possible = min(steps, len(self.prevStack)) 
        
        while possible:  # Step 0
            self.forwardStack.append(self.curPage) # Step 1
            self.curPage = self.prevStack.pop() # Step 2
            possible -= 1 # Step 3 
        
            
        return self.curPage # We need to return the page we're at currently
    

    def forward(self, steps: int) -> str:
        
        possible = min(steps, len(self.forwardStack)) 
        
        while possible:  # Step 0
            self.prevStack.append(self.curPage) # Step 1
            self.curPage = self.forwardStack.pop() # Step 2
            possible -= 1 # Step 3
        
        return self.curPage # We need to return the page we're at currently