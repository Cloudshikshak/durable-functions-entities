import azure.functions as func
import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):
    entityId = df.EntityId("IncrementCounter", "inc1")
    current_value = yield context.call_entity(entityId, "add", 1)
    return current_value

main = df.Orchestrator.create(orchestrator_function)