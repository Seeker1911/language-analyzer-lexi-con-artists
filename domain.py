from lexicon import *

class Domain(Lexicon):
    def __init__(self):
        Lexicon.__init__(self, domain_lexicon)



domain_lexicon = {
    'financial': {
        'achieve': 1,
        'advance': 1,
        'blessings': 1,
        'bribe': 1,
        'buy': 1,
        'credit': 1,
        'development': 1,
        'earned': 1,
        'exemption': 1,
        'million': 1,
        'money': 1,
        'offer': 1,
        'office': 1,
        'rewarded': 1,
        'richest': 1,
        'rising': 1,
        'spend': 1,
        'spends': 1,
        'wealth': 1,
        'worth': 1
    },
    'behavioral': {
        'ability': 1,
        'absurd': 1,
        'against': 1,
        'age': 1,
        'allowing': 1,
        'american': 1,
        'anger': 1,
        'arduous': 1,
        'arguments': 1,
        'attitude': 1,
        'aura': 1,
        'being': 1,
        'belief': 1,
        'believe': 1,
        'cares': 1,
        'cautious': 1,
        'celebrate': 1,
        'cocky': 1,
        'confidence': 1,
        'confident': 1,
        'cruel': 1,
        'cruelty': 1,
        'dance': 1,
        'dare': 1,
        'depressed': 1,
        'desire': 1,
        'dispositions': 1,
        'eager': 1,
        'emotional': 1,
        'emotions': 1,
        'enjoyed': 1,
        'enthusiasm': 1,
        'fear': 1,
        'fearful': 1,
        'fighting': 1,
        'foolish': 1,
        'generous': 1,
        'habit': 1,
        'happiness': 1,
        'ignorance': 1,
        'impress': 1,
        'intelligence': 1,
        'journey': 1,
        'judgmental': 1,
        'manipulate': 1,
        'motivate': 1,
        'negative': 1,
        'negativity': 1,
        'positivity': 1,
        'regard': 1,
        'relations': 1,
        'reputation': 1,
        'satisfied': 1,
        'scared': 1,
        'scoundrels': 1,
        'selfdiscipline': 1,
        'selfknowledge': 1,
        'sensible': 1,
        'sharing': 1,
        'silliness': 1,
        'sorry': 1,
        'soul': 1,
        'strong': 1,
        'subconscious': 1,
        'surefootedness': 1,
        'sweet': 1,
        'thank': 1,
        'threatening': 1,
    },
    'scientific': {
        'achieve': 1,
        'action': 1,
        'amazing': 1,
        'appear': 1,
        'arguments': 1,
        'attainment': 1,
        'blooming': 1,
        'bodies': 1,
        'case': 1,
        'challenge': 1,
        'civilization': 1,
        'conclusion': 1,
        'creation': 1,
        'definite': 1,
        'diet': 1,
        'discover': 1,
        'discovers': 1,
        'doubtful': 1,
        'drug': 1,
        'earth': 1,
        'encounter': 1,
        'evidence': 1,
        'experiment': 1,
        'experimenting': 1,
        'experiments': 1,
        'exploration': 1,
        'fact': 1,
        'fingerprint': 1,
        'ideas': 1,
        'impact': 1,
        'mankind': 1,
        'mental': 1,
        'moon': 1,
        'preserve': 1,
        'project': 1,
        'psychological': 1,
        'render': 1,
        'rising': 1,
        'scientific': 1,
        'sensible': 1,
        'space': 1,
        'state': 1,
        'study': 1,
        'subconscious': 1,
        'succeed': 1,
        'think': 1,
        'thinking': 1,
        'truth': 1,
        'unique': 1,
        'universe': 1,
        'validates': 1
    },
    'educational': {
        'achieve': 1,
        'amazing': 1,
        'attainment': 1,
        'behind': 1,
        'best': 1,
        'bottom': 1,
        'case': 1,
        'challenge': 1,
        'civilization': 1,
        'class': 1,
        'conclusion': 1,
        'country': 1,
        'date': 1,
        'development': 1,
        'discover': 1,
        'discovers': 1,
        'earth': 1,
        'experiment': 1,
        'experimenting': 1,
        'experiments': 1,
        'exploration': 1,
        'fact': 1,
        'history': 1,
        'ideas': 1,
        'project': 1,
        'read': 1,
        'study': 1,
        'succeed': 1,
        'teachings': 1,
        'think': 1,
        'thinking': 1,
        'truth': 1
    },
    'politics': {
        'action': 1,
        'against': 1,
        'aimed': 1,
        'american': 1,
        'anger': 1,
        'angry': 1,
        'apache': 1,
        'arduous': 1,
        'arguments': 1,
        'assembly': 1,
        'banner': 1,
        'battle': 1,
        'belief': 1,
        'believe': 1,
        'bodies': 1,
        'bribe': 1,
        'buy': 1,
        'civilization': 1,
        'conflict': 1,
        'congress': 1,
        'country': 1,
        'debates': 1,
        'decision': 1,
        'defects': 1,
        'defending': 1,
        'demand': 1,
        'democracy': 1,
        'disappointment': 1,
        'drama': 1,
        'evil': 1,
        'foolish': 1,
        'freedom': 1,
        'government': 1,
        'hostages': 1,
        'ideas': 1,
        'impact': 1,
        'intelligence': 1,
        'majority': 1,
        'manipulate': 1,
        'military': 1,
        'missiles': 1,
        'negative': 1,
        'negativity': 1,
        'office': 1,
        'opinion': 1,
        'oppression': 1,
        'oppressive': 1,
        'pander': 1,
        'parties': 1,
        'passions': 1,
        'politics': 1,
        'raid': 1,
        'relations': 1,
        'relationships': 1,
        'republic': 1,
        'republican': 1,
        'resistance': 1,
        'role': 1,
        'service': 1,
        'state': 1,
        'terrorists': 1,
        'threatening': 1,
        'tortured': 1,
        'war': 1
    },
    'relationships': {
        'advance': 1,
        'anger': 1,
        'angry': 1,
        'arduous': 1,
        'arguments': 1,
        'attitude': 1,
        'battle': 1,
        'belief': 1,
        'believe': 1,
        'blessings': 1,
        'bodies': 1,
        'brothers': 1,
        'calling': 1,
        'cares': 1,
        'celebrate': 1,
        'confidence': 1,
        'confident': 1,
        'conflict': 1,
        'dance': 1,
        'date': 1,
        'debates': 1,
        'defects': 1,
        'demand': 1,
        'desire': 1,
        'disappointment': 1,
        'drama': 1,
        'embrace': 1,
        'emotional': 1,
        'emotions': 1,
        'encouraging': 1,
        'friendship': 1,
        'human': 1,
        'humans': 1,
        'manipulate': 1,
        'marriage': 1,
        'parties': 1,
        'passions': 1,
        'regard': 1,
        'rekindle': 1,
        'relations': 1,
        'relationships': 1,
        'role': 1,
        'sharing': 1,
        'sorry': 1,
        'space': 1,
        'talk': 1,
        'thank': 1,
        'threatening': 1,
        'truth': 1
    }
}
