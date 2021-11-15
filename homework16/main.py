# Пользователи должны иметь возможность создавать задания, добавлять в группы задания
# Задать настройки какие-нибудь пользователю
# Получить задачи по группам, сегодняшние, задать дату выполнения задачи, выполнить задачу, удалить, изменить


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Group, Task
import datetime
if __name__ == '__main__':
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

    # User.metadata.drop_all(engine)
    # Group.metadata.drop_all(engine)
    # Task.metadata.drop_all(engine)
    #
    # User.metadata.create_all(engine)
    # Group.metadata.create_all(engine)
    # Task.metadata.create_all(engine)

    Session = sessionmaker(engine)

    with Session() as session:
        user = User(
            telegram_id=1,
        )
        session.add(user)
        session.flush()

        group = Group(
            user_id=user.id,
            name="Work",
        )
        session.add(group)
        session.flush()

        session.add(Task(
            user_id=user.id,
            group_id=group.id,
            description="Work hard",
            when_date=datetime.date.today(),
            place="Skeemans",
        ))
        session.add(Task(
            user_id=user.id,
            description="HOME REST",
            when_date=datetime.date.today(),
            place="Home",
        ))
        session.commit()
