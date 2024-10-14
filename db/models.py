from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


# Модель для клієнтів
class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=True)

    credits = relationship("Credit", back_populates="client")  # Зв'язок з кредитами

    def __repr__(self):
        return f"<Client(name={self.name}, email={self.email})>"


# Модель для кредитів
class Credit(Base):
    __tablename__ = 'credits'

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)
    currency = Column(String, nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'))  # Зв'язок із клієнтом

    client = relationship("Client", back_populates="credits")

    def __repr__(self):
        return f"<Credit(amount={self.amount}, currency={self.currency})>"
