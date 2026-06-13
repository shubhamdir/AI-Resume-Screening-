from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    resume_id:int
    job_description:str