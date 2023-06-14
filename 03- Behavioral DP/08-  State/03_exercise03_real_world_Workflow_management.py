
#state  Pending -> In Progress -> Completed
from abc import ABC, abstractmethod


class WorkflowState(ABC):
    @abstractmethod
    def handle_workflow(self, workflow):
        pass

class PendingState(WorkflowState):
    def handle_workflow(self, workflow):
        print("Handling workflow in the Pending state.")
        # Perform operations specific to the Pending state
        workflow.state = InProgressState()

class InProgressState(WorkflowState):
    def handle_workflow(self, workflow):
        print("Handling workflow in the In Progress state.")
        # Perform operations specific to the Pending state
        workflow.state = CompletedState()

class CompletedState(WorkflowState):
    def handle_workflow(self, workflow):
        print("Workflow is already completed.")
        workflow.state= None


# context - Workflow
class Workflow:
    def __init__(self):
        self.state = PendingState()

    def handle(self):
        self.state.handle_workflow(self)


#usage 

workflow = Workflow()

while True:
    if workflow.state is None:
        break 
    workflow.handle() 
     