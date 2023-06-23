import pytest
from cli import generate_summary

@pytest.fixture
def get_function(): 
    return generate_summary

def test_non_string_input():
    with pytest.raises(TypeError):
        generate_summary(123)

def test_generator():
    sample_text = """Global leaders gathered at the Climate Summit this week to address the pressing issue of climate change. The summit emphasized the urgent need for action, building upon previous agreements like the Paris Agreement. Discussions focused on reducing greenhouse gas emissions, transitioning to clean energy, and adapting to climate impacts. Scientific data showcased alarming trends, such as rising sea levels and extreme weather events. Many nations pledged ambitious targets, aiming for net-zero emissions and significant emission reductions. The summit also highlighted the importance of public support, with youth activists and indigenous leaders advocating for climate justice. Challenges remain, including the need for financial assistance and technology transfer to developing nations. Overall, the summit generated renewed commitment, emphasizing the shared responsibility to combat climate change and work towards a sustainable future."""
    summary = generate_summary(sample_text)
    len(summary) <= len(sample_text)
