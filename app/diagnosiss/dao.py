from app.dao.base import BaseDAO
from app.diagnosiss.models import Diagnosis


class DiagnosisDAO(BaseDAO):
    model = Diagnosis