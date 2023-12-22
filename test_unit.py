import pytest
from datetime import datetime
from main import VisitJournal
import csv


class TestVisitJournal:
    @pytest.fixture
    def visit_journal(self):
        return VisitJournal()

    def test_add_client(self, visit_journal):
        visit_journal.add_client('Doe', 'Toyota', datetime.now())
        assert len(visit_journal.clients) == 1

    def test_remove_client(self, visit_journal):
        visit_journal.add_client('Doe', 'Toyota', datetime.now())
        visit_journal.remove_client('Doe', 'Toyota')
        assert len(visit_journal.clients) == 0

    def test_change_last_name(self, visit_journal):
        visit_journal.add_client('Doe', 'Toyota', datetime.now())
        visit_journal.change_last_name('Doe', 'Smith')
        assert visit_journal.clients[0]['last_name'] == 'Smith'

    def test_change_car_brand(self, visit_journal):
        visit_journal.add_client('Doe', 'Toyota', datetime.now())
        visit_journal.change_car_brand('Doe', 'Honda')
        assert visit_journal.clients[0]['car_brand'] == 'Honda'

    def test_change_days_parked(self, visit_journal):
        visit_journal.add_client('Doe', 'Toyota', datetime.now())
        visit_journal.change_days_parked('Doe', 5)
        assert visit_journal.clients[0]['days_parked'] == 5

    def test_check_client_existence(self, visit_journal):
        visit_journal.add_client('Doe', 'Toyota', datetime.now())
        assert visit_journal.check_client_existence('Doe', 'Toyota') == True

    def test_sort_by_last_name(self, visit_journal):
        visit_journal.add_client('Doe', 'Toyota', datetime.now())
        visit_journal.add_client('Smith', 'Honda', datetime.now())
        visit_journal.sort_by_last_name()
        assert visit_journal.clients[0]['last_name'] == 'Doe'
        assert visit_journal.clients[1]['last_name'] == 'Smith'

    @pytest.mark.parametrize("filename", ["test.csv", "nonexistent_file.csv"])
    def test_read_from_file(self, visit_journal, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['last_name', 'car_brand',
                          'entry_date', 'exit_from_parking', 'days_parked']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({
                'last_name': 'Doe',
                'car_brand': 'Toyota',
                'entry_date': datetime.now().strftime('%Y-%m-%d'),
                'exit_from_parking': '',
                'days_parked': '3'
            })

        visit_journal.read_from_file(filename)
        assert len(visit_journal.clients) == 1
        assert visit_journal.clients[0]['last_name'] == 'Doe'
        assert visit_journal.clients[0]['car_brand'] == 'Toyota'
        assert visit_journal.clients[0]['days_parked'] == 3

    @pytest.mark.parametrize("filename", ["test.csv", "nonexistent_file.csv"])
    def test_write_to_file(self, visit_journal, filename):
        visit_journal.add_client('Doe', 'Toyota', datetime.now())
        visit_journal.write_to_file(filename)

        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            assert len(rows) == 1
            assert rows[0]['last_name'] == 'Doe'
            assert rows[0]['car_brand'] == 'Toyota'



