from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Base(declarative_base):
    pass



class Dim_Gemeente(Base):
    __tablename__ = "Gemeente"
    id: Mapped[int] = mapped_column(primary_key=True)
    gemeente_code:  Mapped[int]
    gemeente_name: Mapped[str]


class Dim_Provincie(Base):
    __tablename__ = "Provincie"
    id: Mapped[int] = mapped_column(primary_key=True)
    naam: Mapped[str]


class FactStudentNumbers(Base):
    __tablename__ = "Student"
    id: Mapped[int] = mapped_column(primary_key = True)
    gemeente_id: Mapped[int] = mapped_column(ForeignKey(Dim_Gemeente.id))
    provincie_id: Mapped[int] = mapped_column(ForeignKey(Dim_Provincie.id))









