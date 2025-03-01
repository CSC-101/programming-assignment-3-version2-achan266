import data
import build_data
import unittest


# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]


def get_sample_datas():
    """Returns a reduced dataset for testing purposes."""
    return [
        CountyDemographics(
            {}, 'County A', {}, {}, {}, {'2014 Population': 100000}, 'CA'
        ),
        CountyDemographics(
            {}, 'County B', {}, {}, {}, {'2014 Population': 200000}, 'CA'
        ),
        CountyDemographics(
            {}, 'County C', {}, {}, {}, {'2014 Population': 150000}, 'TX'
        )
    ]


class TestCases(unittest.TestCase):
    pass

    # Part 1
    @staticmethod
    def get_sample_data():
        """Returns a reduced dataset for testing purposes."""
        return [
            CountyDemographics(
                {}, 'County A', {}, {}, {}, {'2014 Population': 100000}, 'State X'
            ),
            CountyDemographics(
                {}, 'County B', {}, {}, {}, {'2014 Population': 200000}, 'State Y'
            )
        ]

    class TestPopulationTotal(unittest.TestCase):
        def test_population_total_small(self):
            """Test population_total with a small dataset."""
            sample_data = get_sample_data()
            self.assertEqual(population_total(sample_data), 300000)

        def test_population_total_empty(self):
            """Test population_total with an empty list."""
            self.assertEqual(population_total([]), 0)

        def test_population_total_large(self):
            """Test population_total with a large dataset including expected full data set value."""
            from build_data import get_data
            full_datas = get_data()
            self.assertEqual(population_total(full_datas), 318857056)

    # Part 2
    import unittest

    class Testpopulationtotal(unittest.TestCase):
        def test_population_total_small(self):
            """Test population_total with a small dataset."""
            sample_data = get_sample_data()
            self.assertEqual(population_total(sample_data), 450000)

        def test_population_total_empty(self):
            """Test population_total with an empty list."""
            self.assertEqual(population_total([]), 0)

        def test_population_total_large(self):
            """Test population_total with a large dataset including expected full data set value."""
            from build_data import get_data
            full_datas = get_data()
            self.assertEqual(population_total(full_datas), 318857056)

    class TestFilterByState(unittest.TestCase):
        def test_filter_by_state_found(self):
            """Test filter_by_state with a state that exists in the dataset."""
            sample_data = get_sample_data()
            filtered = filter_by_state(sample_data, 'CA')
            self.assertEqual(len(filtered), 2)
            self.assertTrue(all(county.state == 'CA' for county in filtered))

        def test_filter_by_state_not_found(self):
            """Test filter_by_state with a state that does not exist in the dataset."""
            sample_data = get_sample_data()
            filtered = filter_by_state(sample_data, 'NY')
            self.assertEqual(len(filtered)), second
    # Part 3
    @staticmethod
    def get_sample_datas():
        """Returns a reduced dataset for testing purposes."""
        return [
            CountyDemographics(
                {'Percent 65 and Older': 20.0}, 'County A',
                {"Bachelor's Degree or Higher": 30.0},
                {'Hispanic or Latino': 25.0},
                {'Persons Below Poverty Level': 10.0}, {'2014 Population': 100000}, 'CA'
            ),
            CountyDemographics(
                {'Percent 65 and Older': 15.0}, 'County B',
                {"Bachelor's Degree or Higher": 40.0},
                {'Hispanic or Latino': 20.0},
                {'Persons Below Poverty Level': 15.0}, {'2014 Population': 200000}, 'CA'
            )
        ]
    # test population_by_education
    class TestPopulationByEducation(unittest.TestCase):
        def test_population_by_education(self):
            """Test population_by_education for Bachelor's Degree or Higher."""
            sample_data = get_sample_data()
            result = population_by_education(sample_data, "Bachelor's Degree or Higher")
            self.assertEqual(result, 110000.0)

        def test_population_by_education_key_not_found(self):
            """Test population_by_education with a non-existent key."""
            sample_data = get_sample_data()
            result = population_by_education(sample_data, "Some Nonexistent Key")
            self.assertEqual(result, 0)

    # test population_by_ethnicity
    class TestPopulationByEthnicity(unittest.TestCase):
        def test_population_by_ethnicity(self):
            """Test population_by_ethnicity for Hispanic or Latino."""
            sample_data = get_sample_data()
            result = population_by_ethnicity(sample_data, 'Hispanic or Latino')
            self.assertEqual(result, 65000.0)

        def test_population_by_ethnicity_key_not_found(self):
            """Test population_by_ethnicity with a non-existent key."""
            sample_data = get_sample_data()
            result = population_by_ethnicity(sample_data, 'Nonexistent Ethnicity')
            self.assertEqual(result, 0)
    # test population_below_poverty_level
    class TestPopulationBelowPovertyLevel(unittest.TestCase):
        def test_population_below_poverty_level(self):
            """Test population_below_poverty_level for total subpopulation below poverty level."""
            sample_data = get_sample_data()
            result = population_below_poverty_level(sample_data)
            self.assertEqual(result, 40000.0)

        def test_population_below_poverty_level_empty(self):
            """Test population_below_poverty_level with an empty dataset."""
            result = population_below_poverty_level([])
            self.assertEqual(result, 0)
    # Part 4
    # test percent_by_education
    def percent_by_education(self: list[CountyDemographics], education_key: str) -> float:
        """
        Calculate the percentage of the 2014 population with the specified education level
        across a list of counties.

        Args:
            self: A list of CountyDemographics objects.
            education_key: The education level of interest (e.g., "Bachelor's Degree or Higher").

        Returns:
            The percentage of the 2014 population with the specified education level.
        """
        total_population = 0
        total_education_population = 0

        for county in self:
            total_population += county.population['2014 Population']
            if education_key in county.education:
                total_education_population += (county.education[education_key] / 100) * county.population[
                    '2014 Population']

        if total_population == 0:
            return 0.0

        return (total_education_population / total_population) * 100
    def test_percent_by_education(self):
        counties = get_data()  # Assuming this returns a list of CountyDemographics objects
        result = percent_by_education(counties, "Bachelor's Degree or Higher")
        self.assertAlmostEqual(result, 31.5, places=1)  # Example expected value
    # test percent_by_ethnicity
    def percent_by_ethnicity(self: list[CountyDemographics], ethnicity_key: str) -> float:
        total_population = 0
        total_ethnicity_population = 0

        for county in self:
            total_population += county.population['2014 Population']
            if ethnicity_key in county.ethnicities:
                total_ethnicity_population += (county.ethnicities[ethnicity_key] / 100) * county.population[
                    '2014 Population']

        if total_population == 0:
            return 0.0

        return (total_ethnicity_population / total_population) * 100
    def test_percent_by_ethnicity(self):
        counties = get_data()
        result = percent_by_ethnicity(counties, 'Hispanic or Latino')
        self.assertAlmostEqual(result, 22.0, places=1)  # Example expected value
    # test percent_below_poverty_level
    def percent_below_poverty_level(self: list[CountyDemographics]) -> float:

        pass

    # Part 5
    # test education_greater_than
    def education_greater_than(self: list[CountyDemographics], education_key: str, threshold: float) -> list[
        CountyDemographics]:
        return [county for county in self if
                education_key in county.education and county.education[education_key] > threshold]

    def test_education_greater_than(self):
        result = education_greater_than(self.counties, "Bachelor's Degree or Higher", 30.0)
        self.assertTrue(all(county.education["Bachelor's Degree or Higher"] > 30.0 for county in result))
    # test education_less_than
    @staticmethod
    def education_less_than(education_key: str, threshold: float) -> list[
        CountyDemographics]:
        return [county for county in counties if
                education_key in county.education and county.education[education_key] < threshold]

    def test_education_less_than(self):
        result = education_less_than(self.counties, "Bachelor's Degree or Higher", 20.0)
        self.assertTrue(all(county.education["Bachelor's Degree or Higher"] < 20.0 for county in result))
    # test ethnicity_greater_than
    @staticmethod
    def ethnicity_greater_than(ethnicity_key: str, threshold: float) -> list[
        CountyDemographics]
        return [county for county in counties if
                ethnicity_key in county.ethnicities and county.ethnicities[ethnicity_key] > threshold]

    def test_ethnicity_greater_than(self):
        result = ethnicity_greater_than(self.counties, 'Hispanic or Latino', 25.0)
        self.assertTrue(all(county.ethnicities['Hispanic or Latino'] > 25.0 for county in result))
    # test ethnicity_less_than
    @staticmethod
    def ethnicity_less_than(ethnicity_key: str, threshold: float) -> list[
        CountyDemographics]:
        return [county for county in counties if
                ethnicity_key in county.ethnicities and county.ethnicities[ethnicity_key] < threshold]

    def test_ethnicity_less_than(self):
        result = ethnicity_less_than(self.counties, 'Hispanic or Latino', 10.0)
        self.assertTrue(all(county.ethnicities['Hispanic or Latino'] < 10.0 for county in result))
    # test below_poverty_level_greater_than
    def below_poverty_level_greater_than(self: list[CountyDemographics], threshold: float) -> list[
        CountyDemographics]:

    def test_below_poverty_level_greater_than(self):
            result = below_poverty_level_greater_than(self.counties, 20.0)
            self.assertTrue(all(county.income['Persons Below Poverty Level'] > 20.0 for county in result))

    # test below_poverty_level_less_than


def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if
            'Persons Below Poverty Level' in county.income and county.income['Persons Below Poverty Level'] < threshold]
def test_below_poverty_level_less_than(self):
        result = below_poverty_level_less_than(self.counties, 10.0)
        self.assertTrue(all(county.income['Persons Below Poverty Level'] < 10.0 for county in result))

if __name__ == '__main__':
    unittest.main()
