from slyguy.settings import CommonSettings
from slyguy.settings.types import Bool, Enum, Action
from xbmcaddon import Addon

from .language import _


class Ratio:
    ASK = 'ASK'
    IMAX = 'IMAX'
    WIDESCREEN = 'WIDESCREEN'


class Settings(CommonSettings):
    PLAY_NEXT_EPISODE = Bool('play_next_episode', _.PLAY_NEXT_EPISODE, default=True)
    PLAY_NEXT_MOVIE = Bool('play_next_movie', _.PLAY_NEXT_MOVIE, default=False)
    SKIP_INTROS = Bool('skip_intros', _.SKIP_INTROS, default=False)
    SKIP_CREDITS = Bool('skip_credits', _.SKIP_CREDITS, default=True)
    SYNC_WATCHLIST = Bool('sync_watchlist', _.DISNEY_WATCHLIST, default=True)
    SYNC_PLAYBACK = Bool('sync_playback', _.DISNEY_SYNC, default=False)
    DEFAULT_RATIO = Enum('default_ratio', _.DEFAULT_RATIO, default=Ratio.ASK, loop=True,
                    options=[[_.ASK, Ratio.ASK], [_.IMAX, Ratio.IMAX], [_.WIDESCREEN, Ratio.WIDESCREEN]])
    USE_TTML2SSA = Bool('use_ttml2ssa', default=True, label=Addon('script.module.ttml2ssa').getLocalizedString(32202))
    SSA_SETTINGS = Action("Addon.OpenSettings(script.module.ttml2ssa)", label=Addon('script.module.ttml2ssa').getLocalizedString(32201))



settings = Settings()
