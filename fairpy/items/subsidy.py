from fairpy import AgentList
from typing import List, Any
from fairpy.allocations import Allocation

class Subsidy:
    """
    Represents an allocation of money to agents
    """
    pass


class AllocationWithSubsidy(Allocation):
    """
    A class extending the Allocation class. Contains both allocation and a subsidy for each agent
    """
    pass


def allocate_with_subsidy(agents: AgentList) -> AllocationWithSubsidy:
    """
    Article: 
        Fair Division with Subsidy 
        Daniel Halpern and Nisarg Shah
        2019
        http://www.cs.toronto.edu/%7enisarg/papers/subsidy.pdf

    The article does not spell out any specific algorithm but only prove it's correctness. So, no specific algorithm number.

    The algorithm takes a list of agents, chooses an algorithm, finds an allocation with bounded subsidy an returns it.

    Programmer: Tal Zichlinsky

    ### Example 1 - Two Agents, One Item, Non-binary:
    >>> from fairpy import AdditiveAgent
    >>> alice = AdditiveAgent({"ring": 100}, name="Alice")
    >>> bob = AdditiveAgent({"ring": 150}, name="Bob")
    >>> allocation_with_subsidy = allocate_with_subsidy(AgentList([alice, bob])) # Bob gets ring, Alice gets subsidy of 100

    ### Example 2 - Three Agents, Three Items, Binary:
    >>> alice = AdditiveAgent({"a": 1, "b": 0, "c": 0}, name="Alice")
    >>> bob = AdditiveAgent({"a": 0, "b": 1, "c": 0}, name="Bob")
    >>> charlie = AdditiveAgent({"a": 0, "b": 0, "c": 1}, name="Charlie")
    >>> allocation_with_subsidy = allocate_with_subsidy(AgentList([alice, bob, charlie])) # Alice gets a, Bob gets b, Charlie gets c. No subsidy

    ### Example 3 - Three Agents, Three Items, Binary:
    >>> alice = AdditiveAgent({"a": 1, "b": 1, "c": 1}, name="Alice")
    >>> bob = AdditiveAgent({"a": 1, "b": 1, "c": 1}, name="Bob")
    >>> charlie = AdditiveAgent({"a": 1, "b": 1, "c": 1}, name="Charlie")
    >>> allocation_with_subsidy = allocate_with_subsidy(AgentList([alice, bob, charlie])) # Alice gets a, Bob gets b, Charlie gets c. No subsidy

    ### Example 4 - Two Agents, Three Items, Binary:
    >>> alice = AdditiveAgent({"a": 1, "b": 1, "c": 0}, name="Alice")
    >>> bob = AdditiveAgent({"a": 1, "b": 1, "c": 1}, name="Bob")
    >>> allocation_with_subsidy = allocate_with_subsidy(AgentList([alice, bob])) # Alice gets a and c, Bob gets b and subsidy of 1

    ### Example 5 - No Agents
    >>> allocation_with_subsidy = allocate_with_subsidy(AgentList([])) # []
    
    ### Example 6 - No Items
    >>> alice = AdditiveAgent({}, name="Alice")
    >>> bob = AdditiveAgent({}, name="Bob")
    >>> allocation_with_subsidy = allocate_with_subsidy(AgentList([])) # []
    """
    pass
