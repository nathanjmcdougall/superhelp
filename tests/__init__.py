
from nose.tools import assert_equal, assert_not_equal, assert_true, assert_false  # @UnusedImport @UnresolvedImport

from superhelp import conf
from superhelp.messages import get_separated_messages_dets

def get_actual_source_freqs(messages_dets, expected_source_freqs):
    """
    Check the message sources are as expected. Note - we don't have to know what
    messages generated from advisors in other modules will do - just what we
    expect from this module. So we don't specify what sources we expect - just
    those that we require (and how often) and those we ban (we expect those 0
    times).

    :param list messages_dets: list of MessageDets named tuples
    :param dict expected_source_freqs: keys are sources (strings) and values are
     integers. The integer should be set to 0 if we want to explicitly ban a
     source i.e. we do not expect it provide a message. E.g. if our list does
     not have mixed data types we do not expect a message saying there are.
    :return: whether it is as expected or not
    :rtype: bool
    """
    overall_snippet_messages_dets, block_level_messages_dets = messages_dets
    all_messages_dets = (
        overall_snippet_messages_dets + block_level_messages_dets)
    actual_source_freqs = {source: 0 for source in expected_source_freqs}
    for message_dets in all_messages_dets:
        if message_dets.source in expected_source_freqs:
            actual_source_freqs[message_dets.source] += 1  ## if we track any sources not in the expected list the dicts will vary even if the results for the tracked sources are exactly as expected and we'll fail the test when we shouldn't)
    return actual_source_freqs

def check_as_expected(test_conf):
    """
    :param list test_conf: list of tuples: snippet, dict of expected message
     sources and their expected frequencies
    """
    conf.DEV_MODE = True  ## updates XML so we can check what is happening :-)
    for snippet, expected_source_freqs in test_conf:
        messages_dets = get_separated_messages_dets(snippet)
        actual_source_freqs = get_actual_source_freqs(
            messages_dets, expected_source_freqs)
        assert_equal(actual_source_freqs, expected_source_freqs,
            (f"\n\nSnippet\n\n{snippet}\n\n"
             "didn't get messages as expected from the sources:"
             f"\n\nExpected:\n{expected_source_freqs}"
             f"\n\nActual:\n{actual_source_freqs}"
            )
        )