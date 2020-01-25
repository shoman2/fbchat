import datetime
from fbchat import EmojiSet, Group, User


def test_emoji_set_fetch(session):
    data = {
        "__typename": "GenericAdminTextMessage",
        "message_id": "mid.$XYZ",
        "offline_threading_id": "1122334455",
        "message_sender": {"id": "1234", "email": "1234@facebook.com",},
        "ttl": 0,
        "timestamp_precise": "1500000000000",
        "unread": True,
        "is_sponsored": False,
        "ad_id": None,
        "ad_client_token": None,
        "commerce_message_type": None,
        "customizations": [],
        "tags_list": [
            "inbox",
            "sent",
            "no_push",
            "tq",
            "blindly_apply_message_folder",
            "source:titan:web",
        ],
        "platform_xmd_encoded": None,
        "message_source_data": None,
        "montage_reply_data": None,
        "message_reactions": [],
        "unsent_timestamp_precise": "0",
        "message_unsendability_status": "deny_log_message",
        "extensible_message_admin_text": {
            "__typename": "ThreadIconExtensibleMessageAdminText",
            "thread_icon": "😊",
        },
        "extensible_message_admin_text_type": "CHANGE_THREAD_ICON",
        "snippet": "You set the emoji to 😊.",
        "replied_to_message": None,
    }
    thread = Group(session=session, id="4321")
    assert EmojiSet(
        author=User(session=session, id="1234"),
        thread=thread,
        emoji="😊",
        at=datetime.datetime(2017, 7, 14, 2, 40, tzinfo=datetime.timezone.utc),
    ) == EmojiSet._from_fetch(thread, data)
