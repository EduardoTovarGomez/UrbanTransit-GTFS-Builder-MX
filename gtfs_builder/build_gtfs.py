from gtfs_builder import config

from gtfs_builder.exporter import GTFSExporter
from gtfs_builder.parser import KMLParser
from gtfs_builder.route_matcher import RouteMatcher
from gtfs_builder.schedule_generator import ScheduleGenerator
from gtfs_builder.time_engine import TimeEngine
from gtfs_builder.trip_generator import TripGenerator
from gtfs_builder.ui import ConsoleUI
from gtfs_builder.validator import ProjectValidator


def main():

    ui = ConsoleUI()
    ui.banner()

    # =====================================================
    # LOAD PROJECT
    # =====================================================

    parser = KMLParser(config.INPUT_KML)

    parser.load()
    parser.parse()

    routes = parser.routes
    stops = parser.stops

    # =====================================================
    # VALIDATION
    # =====================================================

    validator = ProjectValidator(parser)
    validator.validate()

    # =====================================================
    # ROUTE MATCHING
    # =====================================================

    matcher = RouteMatcher(
        routes,
        stops
    )

    matcher.match()

    # =====================================================
    # TIME ENGINE
    # =====================================================

    time_engine = TimeEngine()

    for route in routes:

        time_engine.build_shape_distances(route)

        time_engine.assign_stop_distances(route)

        time_engine.calculate_travel_times(route)

    # =====================================================
    # GTFS OBJECTS
    # =====================================================

    trip_generator = TripGenerator()

    trips = trip_generator.generate(
        routes
    )

    schedule_generator = ScheduleGenerator()

    stop_times = schedule_generator.generate(
        trips,
        routes
    )

    # =====================================================
    # EXPORT
    # =====================================================

    exporter = GTFSExporter()

    exporter.export_stops(stops)
    exporter.export_routes(routes)
    exporter.export_shapes(routes)
    exporter.export_trips(trips)
    exporter.export_stop_times(stop_times)
    exporter.export_agency()
    exporter.export_calendar()
    exporter.export_feed_info()
    exporter.export_zip()

    # =====================================================
    # FINISH
    # =====================================================

    ui.finish(parser)


if __name__ == "__main__":

    main()