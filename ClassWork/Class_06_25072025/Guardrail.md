# Understanding Guardrails in AI Agents 🛡️

This document explains the implementation of guardrails in our AI agent system, which helps control and validate both input and output of the AI responses.

## Overview

Guardrails are safety mechanisms that help ensure AI agents behave within specified boundaries. In our implementation, we have two types of guardrails:
1. Input Guardrail (Math Homework Check)
2. Output Guardrail (Physics Homework Check)

## Implementation Details

### Input Guardrail

```python
@input_guardrail
async def math_guardrail(ctx, agent, input):
    result = await Runner.run(starting_agent=input_guardrail_agent, input=input)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_math_homework,
    )
```

- **Purpose**: Prevents users from getting help with math homework
- **Process**:
  1. Takes user input
  2. Analyzes it using a dedicated agent
  3. Returns a GuardrailFunctionOutput with:
     - output_info: Contains analysis results
     - tripwire_triggered: Boolean indicating if math homework was detected

### Output Guardrail

```python
@output_guardrail
async def physics_guardrail(ctx, agent, output):
    result = await Runner.run(starting_agent=output_guardrail_agent, input=output.response)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_physics_homework,
    )
```

- **Purpose**: Prevents the agent from providing physics homework help
- **Process**:
  1. Takes agent's output
  2. Analyzes it using a dedicated agent
  3. Returns a GuardrailFunctionOutput with:
     - output_info: Contains analysis results
     - tripwire_triggered: Boolean indicating if physics content was detected

## Output Types

### MathHomeworkOutput
```python
class MathHomeworkOutput(BaseModel):
    is_math_homework: bool
    reasoning: str
```

### PhysicsHomeworkOutput
```python
class PhysicsHomeworkOutput(BaseModel):
    is_physics_homework: bool
    reasoning: str
```

### MainMessageOutput
```python
class MainMessageOutput(BaseModel):
    response: str
```

## Exception Handling

The system uses two custom exceptions:
1. `InputGuardrailTripwireTriggered`: Raised when math homework is detected
2. `OutputGuardrailTripwireTriggered`: Raised when physics homework is detected

Example handling:
```python
try:
    result = await Runner.run(starting_agent=customer_support_agent, input=user_input)
except InputGuardrailTripwireTriggered as e:
    print("Math homework detected:", e.guardrail_result.output.output_info.reasoning)
except OutputGuardrailTripwireTriggered as e:
    print("Physics homework detected:", e.guardrail_result.output.output_info.reasoning)
```

## Best Practices

1. **Clear Instructions**: Each guardrail agent should have clear, specific instructions
2. **Type Safety**: Use Pydantic models to ensure type safety
3. **Meaningful Feedback**: Include reasoning in the output to explain why a guardrail was triggered
4. **Exception Handling**: Always handle guardrail exceptions gracefully

## Example Scenarios

### Math Homework Detection
Input: "Give me the answer of 2 + 2"
Result: Input guardrail triggered ❌

### Physics Homework Detection
Input: "Define newton's third law of motion?"
Result: Output guardrail triggered ❌

### Valid Query
Input: "How do I track my order?"
Result: Passes both guardrails ✅
