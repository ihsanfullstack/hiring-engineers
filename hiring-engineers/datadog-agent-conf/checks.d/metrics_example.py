import random

from datadog_checks.base import AgentCheck

__version__ = "1.0.0"

class MyClass(AgentCheck):
    def check(self, instance):
        # self.count(
        #     "example_metric.count",
        #     2,
        #     tags="metric_submission_type:count",
        # )
        # self.decrement(
        #     "example_metric.decrement",
        #     tags="metric_submission_type:count",
        # )
        # self.increment(
        #     "example_metric.increment",
        #     tags="metric_submission_type:count",
        # )
        # self.rate(
        #     "example_metric.rate",
        #     1,
        #     tags="metric_submission_type:rate",
        # )
        self.gauge(
            "my_metric",
            random.randint(0, 1000),
            tags="metric_submission_type:gauge",
        )
        # self.monotonic_count(
        #     "example_metric.monotonic_count",
        #     2,
        #     tags="metric_submission_type:monotonic_count",
        # )

        # # Calling the functions below twice simulates
        # # several metrics submissions during one Agent run.
        # self.histogram(
        #     "example_metric.histogram",
        #     random.randint(0, 10),
        #     tags="metric_submission_type:histogram",
        # )
        # self.histogram(
        #     "example_metric.histogram",
        #     random.randint(0, 10),
        #     tags="metric_submission_type:histogram",
        # )
