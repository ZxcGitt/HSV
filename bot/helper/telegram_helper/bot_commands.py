from bot import CMD_INDEX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start{CMD_INDEX}'
        self.MirrorCommand = (f'mirror3{CMD_INDEX}', f'm3{CMD_INDEX}')
        self.UnzipMirrorCommand = (f'unzipmirror3{CMD_INDEX}', f'uzm3{CMD_INDEX}')
        self.ZipMirrorCommand = (f'zipmirror3{CMD_INDEX}', f'zm3{CMD_INDEX}')
        self.QbMirrorCommand = (f'qbmirror3{CMD_INDEX}', f'qm3{CMD_INDEX}')
        self.QbUnzipMirrorCommand = (f'qbunzipmirror3{CMD_INDEX}', f'quzm3{CMD_INDEX}')
        self.QbZipMirrorCommand = (f'qbzipmirror3{CMD_INDEX}', f'qzm3{CMD_INDEX}')
        self.YtdlCommand = (f'ytdl3{CMD_INDEX}', f'y3{CMD_INDEX}')
        self.YtdlZipCommand = (f'ytdlzip3{CMD_INDEX}', f'yz3{CMD_INDEX}')
        self.LeechCommand = (f'leech3{CMD_INDEX}', f'l3{CMD_INDEX}')
        self.UnzipLeechCommand = (f'unzipleech3{CMD_INDEX}', f'uzl3{CMD_INDEX}')
        self.ZipLeechCommand = (f'zipleech3{CMD_INDEX}', f'zl3{CMD_INDEX}')
        self.QbLeechCommand = (f'qbleech3{CMD_INDEX}', f'ql3{CMD_INDEX}')
        self.QbUnzipLeechCommand = (f'qbunzipleech3{CMD_INDEX}', f'quzl3{CMD_INDEX}')
        self.QbZipLeechCommand = (f'qbzipleech3{CMD_INDEX}', f'qzl3{CMD_INDEX}')
        self.YtdlLeechCommand = (f'ytdlleech3{CMD_INDEX}', f'yl3{CMD_INDEX}')
        self.YtdlZipLeechCommand = (f'ytdlzipleech3{CMD_INDEX}', f'yzl3{CMD_INDEX}')
        self.CloneCommand = f'clone3{CMD_INDEX}'
        self.CountCommand = f'count3{CMD_INDEX}'
        self.DeleteCommand = f'del3{CMD_INDEX}'
        self.CancelMirror = f'cancel3{CMD_INDEX}'
        self.CancelAllCommand = f'cancelall3{CMD_INDEX}'
        self.ListCommand = f'list3{CMD_INDEX}'
        self.SearchCommand = f'search3{CMD_INDEX}'
        self.StatusCommand = f'status3{CMD_INDEX}'
        self.UsersCommand = f'users3{CMD_INDEX}'
        self.AuthorizeCommand = f'authorize3{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauthorize3{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo3{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudo3{CMD_INDEX}'
        self.PingCommand = f'ping3{CMD_INDEX}'
        self.RestartCommand = f'restart3{CMD_INDEX}'
        self.StatsCommand = f'stats3{CMD_INDEX}'
        self.HelpCommand = f'help3{CMD_INDEX}'
        self.LogCommand = f'log3{CMD_INDEX}'
        self.ShellCommand = f'shell3{CMD_INDEX}'
        self.EvalCommand = f'eval3{CMD_INDEX}'
        self.ExecCommand = f'exec3{CMD_INDEX}'
        self.ClearLocalsCommand = f'clearlocals3{CMD_INDEX}'
        self.UserSetCommand = f'usetting3{CMD_INDEX}'
        self.SetThumbCommand = f'setthumb3{CMD_INDEX}'
        self.BtSelectCommand = f'btsel3{CMD_INDEX}'
        self.RssListCommand = (f'rsslist3{CMD_INDEX}', f'rl3{CMD_INDEX}')
        self.RssGetCommand = (f'rssget3{CMD_INDEX}', f'rg3{CMD_INDEX}')
        self.RssSubCommand = (f'rsssub3{CMD_INDEX}', f'rs3{CMD_INDEX}')
        self.RssUnSubCommand = (f'rssunsub3{CMD_INDEX}', f'rus3{CMD_INDEX}')
        self.RssSettingsCommand = (f'rssset3{CMD_INDEX}', f'rst3{CMD_INDEX}')

BotCommands = _BotCommands()
