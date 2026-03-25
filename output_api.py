"""
Dev 2 — Output API for Dev 3
Formats the final complete output JSON matching Dev 3's expected input schema.
Includes intersection state + city-level state + routes.
"""

import json
from typing import Dict, List, Optional


class OutputAPI:
    """
    Formats Dev 2 pipeline output into the schema Dev 3 expects.
    
    Output structure:
    {
        "intersection_id": "...",
        "timestamp": ...,
        "lanes": [...],
        "sectors": [...],
        "emergency_state": {...},
        "city_state": {...},
        "routes": [...]
    }
    """

    @staticmethod
    def format_output(
        intersection_state: dict,
        city_graph: Optional[dict] = None,
        routes: Optional[List[dict]] = None,
        emergency_geo: Optional[dict] = None,
    ) -> dict:
        """
        Format the complete Dev 2 output for Dev 3.
        
        Args:
            intersection_state: IntersectionState.to_dict()
            city_graph: CityGraph.to_dict() (optional)
            routes: list of Route.to_dict() (optional)
            emergency_geo: emergency vehicle geo-position (optional)
        
        Returns:
            Complete output JSON dict
        """
        output = {
            "intersection_id": intersection_state.get("intersection_id", ""),
            "timestamp": intersection_state.get("timestamp", 0.0),
            "lanes": intersection_state.get("lanes", []),
            "sectors": intersection_state.get("sectors", []),
            "emergency_state": intersection_state.get("emergency_state", {}),
        }

        # Add city-level state if available
        if city_graph:
            output["city_state"] = city_graph
        else:
            output["city_state"] = {"nodes": [], "edges": []}

        # Add routes if available
        if routes:
            output["routes"] = routes
        else:
            output["routes"] = []

        # Add emergency geo position if available
        if emergency_geo:
            output["emergency_position"] = emergency_geo

        return output

    @staticmethod
    def to_json(output: dict, indent: int = 2) -> str:
        """Serialize output to JSON string."""
        return json.dumps(output, indent=indent)

    @staticmethod
    def save_to_file(output: dict, filepath: str):
        """Save output to a JSON file."""
        with open(filepath, "w") as f:
            json.dump(output, f, indent=2)
