from cognitive_nodes.goal import GoalMotiven

class GoalDummy(GoalMotiven):
    """
    Dummy Goal class: A goal that is never rewarded.
    This Goal has the activation value manually given thought /set_activation service.
    """

    def calculate_activation(self, perception = None, activation_list=None):
        """
        Returns the the activation value of the goal

        :param perception: Perception does not influence the activation 
        :type perception: dict
        :return: The activation of the goal
        :rtype: float
        """
        if self.activation_topic:
            self.publish_activation(self.activation)
        return self.activation

    def calculate_reward(self, drive_name): #No reward is provided
        """
        Calculates the reward of the goal based on the evaluation of the Drive node.
        In this case, the reward is always 0.0.

        :param drive_name: Name of the drive node. Not used in this case.
        :type drive_name: str
        :return: The reward value and the timestamp.
        :rtype: tuple
        """
        self.reward = 0.0
        return self.reward, self.get_clock().now().to_msg()