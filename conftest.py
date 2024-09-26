import os
import pytest
import subprocess

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """Hook to send email after all tests are finished"""
    # Generate and send the test report after the test session finishes
    if exitstatus == 0:
        print("All tests passed. Sending email with report...")
    else:
        print("Some tests failed. Sending email with report...")

    # Run the email sending script
    subprocess.run(["python", "send_report.py"])
