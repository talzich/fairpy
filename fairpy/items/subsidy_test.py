import unittest
import fairpy
from subsidy import allocate_with_subsidy


class TestSubsidy(unittest.TestCase):

    def test_normal_case_1(self):
        alice = fairpy.agents.AdditiveAgent({"ring": 100}, name="Alice")
        bob = fairpy.agents.AdditiveAgent({"ring": 150}, name="Bob")

        # Bob gets ring, Alice gets subsidy of 100
        allocation_with_subsidy = allocate_with_subsidy(fairpy.AgentList([alice, bob]))
        self.assertEqual(allocation_with_subsidy, [((), 100), (('ring'), 0)])

    def test_normal_case_2(self):
        alice = fairpy.agents.AdditiveAgent({"a": 1, "b": 0, "c": 0}, name="Alice")
        bob = fairpy.agents.AdditiveAgent({"a": 0, "b": 1, "c": 0}, name="Bob")
        charlie = fairpy.agents.AdditiveAgent({"a": 0, "b": 0, "c": 1}, name="Charlie")

        # Alice gets a, Bob gets b, Charlie gets c. No subsidy
        allocation_with_subsidy = allocate_with_subsidy(fairpy.AgentList([alice, bob, charlie]))
        self.assertEqual(allocation_with_subsidy, [(('a'), 0), (('b'), 0), (('c'), 0)])

    def test_normal_case_3(self):
        alice = fairpy.agents.AdditiveAgent({"a": 1, "b": 1, "c": 1}, name="Alice")
        bob = fairpy.agents.AdditiveAgent({"a": 1, "b": 1, "c": 1}, name="Bob")
        charlie = fairpy.agents.AdditiveAgent({"a": 1, "b": 1, "c": 1}, name="Charlie")

        # Alice gets a, Bob gets b, Charlie gets c. No subsidy
        allocation_with_subsidy = allocate_with_subsidy(fairpy.AgentList([alice, bob, charlie]))
        self.assertEqual(allocation_with_subsidy, [(('a'), 0), (('b'), 0), (('c'), 0)])

    def test_normal_case_4(self):
        alice = fairpy.agents.AdditiveAgent({"a": 1, "b": 1, "c": 1}, name="Alice")
        bob = fairpy.agents.AdditiveAgent({"a": 1, "b": 1, "c": 1}, name="Bob")

        # Alice gets a, Bob gets b, Charlie gets c. No subsidy
        allocation_with_subsidy = allocate_with_subsidy(fairpy.AgentList([alice, bob]))
        self.assertEqual(allocation_with_subsidy, [(('a', 'c'), 0), (('b'), 1)])

    def test_no_agents(self):
        allocation_with_subsidy = allocate_with_subsidy(fairpy.AgentList([]))
        self.assertEqual(allocation_with_subsidy, [])

    def test_no_items(self):
        alice = fairpy.agents.AdditiveAgent(name="Alice")
        bob = fairpy.agents.AdditiveAgent(name="Bob")

        allocation_with_subsidy = allocate_with_subsidy(fairpy.AgentList([alice, bob]))
        self.assertEqual(allocation_with_subsidy, [])
