# import sys
# import os
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Base, Activity, ActivityOption, AppConfig


def seed_database():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        existing_activities = db.query(Activity).count()
        if existing_activities > 0:
            print("Database already seeded. Skipping...")
            return

        activities_data = [
            {
                "order": 1,
                "question": "Where should we go for our anniversary celebration?",
                "options": [
                    {"order": 1, "option_text": "Beach Town"},
                    {"order": 2, "option_text": "Redwood Hike"},
                    # {"order": 3, "option_text": "City weekend adventure"},
                    # {"order": 4, "option_text": "Luxury spa resort"}
                ]
            },
            {
                "order": 2,
                "question": "What type of dining experience should they enjoy?",
                "options": [
                    {"order": 1, "option_text": "Fine dining at a Michelin-star restaurant"},
                    {"order": 2, "option_text": "Private chef cooking class"},
                    {"order": 3, "option_text": "Romantic picnic under the stars"},
                    {"order": 4, "option_text": "Food tour of local cuisine"}
                ]
            },
            {
                "order": 3,
                "question": "What activity should be part of their celebration?",
                "options": [
                    {"order": 1, "option_text": "Couples massage and spa day"},
                    {"order": 2, "option_text": "Hot air balloon ride"},
                    {"order": 3, "option_text": "Wine tasting tour"},
                    {"order": 4, "option_text": "Dance lessons"}
                ]
            },
            {
                "order": 4,
                "question": "What entertainment would make the day special?",
                "options": [
                    {"order": 1, "option_text": "Live music concert or show"},
                    {"order": 2, "option_text": "Private movie screening"},
                    {"order": 3, "option_text": "Comedy club night"},
                    {"order": 4, "option_text": "Sunset cruise"}
                ]
            },
            {
                "order": 5,
                "question": "What keepsake should they create together?",
                "options": [
                    {"order": 1, "option_text": "Professional photo shoot"},
                    {"order": 2, "option_text": "Pottery or art class creation"},
                    {"order": 3, "option_text": "Custom jewelry making"},
                    {"order": 4, "option_text": "Plant a tree together"}
                ]
            },
            {
                "order": 6,
                "question": "How should they end the perfect anniversary day?",
                "options": [
                    {"order": 1, "option_text": "Stargazing with champagne"},
                    {"order": 2, "option_text": "Bonfire on the beach"},
                    {"order": 3, "option_text": "Rooftop dinner at sunset"},
                    {"order": 4, "option_text": "Couples' dance under the stars"}
                ]
            }
        ]

        for activity_data in activities_data:
            activity = Activity(
                order=activity_data["order"],
                question=activity_data["question"],
                is_active=True
            )
            db.add(activity)
            db.flush()

            for option_data in activity_data["options"]:
                option = ActivityOption(
                    activity_id=activity.id,
                    option_text=option_data["option_text"],
                    order=option_data["order"]
                )
                db.add(option)

        config = AppConfig(is_voting_closed=False, voting_end_time=None)
        db.add(config)

        db.commit()
        print("Database seeded successfully with 6 anniversary activities!")

    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
