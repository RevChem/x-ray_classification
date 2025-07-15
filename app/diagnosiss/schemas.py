from pydantic import BaseModel, ConfigDict
from app.diagnosiss.sql_enums import DiagnosisEnum

class SDiagnosisAdd(BaseModel):
    diagnosis: DiagnosisEnum
    image_path: str | None

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)


class SDiagnosisUpdDesc(BaseModel):
    image_path: str | None
