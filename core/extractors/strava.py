from core.connectors.strava import Strava
from core.transformers.filters import StravaFilter
from core.transformers.strava_models import SummaryActivity, DetailedActivity


class StravaExtractor:
    def __init__(self):
        self.con = Strava()
        self.filter = StravaFilter()

    def all_summary_activities(self, after: str = None, before: str = None):
        summary_activities = self.con.activities(after, before)
        filtered = [self.filter.filter_summary_activity(res) for res in summary_activities]
        summary_activities_obj = [SummaryActivity(**res) for res in filtered]
        return summary_activities_obj

    @staticmethod
    def get_activity_id_from_summary_activity(summary_activity: SummaryActivity):
        return summary_activity.id

    def detailed_activity(self, id: int):
        detailed_activity = self.con.detailed_activity(id)
        filtered = self.filter.filter_detailed_activity(detailed_activity)
        detailed_activity_obj = DetailedActivity(**filtered)
        return detailed_activity_obj
