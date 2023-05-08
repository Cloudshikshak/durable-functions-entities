import azure.functions as func
import azure.durable_functions as df

async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    client = df.DurableOrchestrationClient(starter)
    entityId = df.EntityId("IncrementCounter", "inc1")
    
    # Signal entity (one way operation)
    await client.signal_entity(entityId, "add", 1)
    
    entity_state_result = await client.read_entity_state(entityId)
    entity_state = "No state found"
    if entity_state_result.entity_exists:
      entity_state = str(entity_state_result.entity_state)
    return func.HttpResponse(entity_state)
    