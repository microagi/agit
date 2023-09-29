from pyparsing import Literal, Word, alphanums, Optional

# Define literals for git commands and options
git = Literal("git")
commit = Literal("commit")
rebase = Literal("rebase")
merge = Literal("merge")
tag = Literal("tag")
config = Literal("config")
bisect = Literal("bisect")
stash = Literal("stash")
cherry_pick = Literal("cherry-pick")
var = Literal("var")
push = Literal("push")
branch = Literal("branch")
checkout = Literal("checkout")
clean = Literal("clean")
reset = Literal("reset")
rm = Literal("rm")
fsck = Literal("fsck")
gc = Literal("gc")
reflog = Literal("reflog")
update_ref = Literal("update-ref")
filter_branch = Literal("filter-branch")
filter_repo = Literal("filter-repo")

# Define literals for options/flags
m = Literal("-m")
no_edit = Literal("--no-edit")
i = Literal("-i")
interactive = Literal("--interactive")
annotate = Literal("-a")
edit = Literal("--edit")
force = Literal("--force")
f = Literal("-f")
D = Literal("-D")
d = Literal("-d")
B = Literal("-B")
b = Literal("-b")
fd = Literal("-fd")
hard = Literal("--hard")
soft = Literal("--soft")
mixed = Literal("--mixed")
cached = Literal("--cached")
amend = Literal("--amend")
full = Literal("--full")
prune = Literal("--prune=now")
expire = Literal("--expire=now")
all = Literal("--all")
drop = Literal("drop")
clear = Literal("clear")

# Define a word pattern to match command arguments
arg = Word(alphanums + "-_")

# Interactive commmands grammar definitions
commit_command = git + commit + Optional(m + arg)
rebase_command = git + rebase + (i | interactive) + Optional(arg)
merge_command = git + merge + ~no_edit + Optional(arg)
tag_command = git + tag + annotate + ~m + Optional(arg)
config_command = git + config + edit
bisect_command = git + bisect + Literal("run") + Optional(arg)
stash_command = git + stash + (drop | Literal("pop")) + Optional(arg)
cherry_pick_command = git + cherry_pick + ~Literal("--no-commit") + Optional(arg)
var_command = git + var + Literal("GIT_EDITOR")

interactive_commands = [
    commit_command,
    rebase_command,
    merge_command,
    tag_command,
    config_command,
    bisect_command,
    stash_command,
    cherry_pick_command,
    var_command,
]

# Destructive commands grammar definitions
push_command_force = git + push + force + Optional(arg)
push_command_f = git + push + f + Optional(arg)
branch_command_D = git + branch + D + Optional(arg)
branch_command_d = git + branch + d + Optional(arg)
checkout_command_B = git + checkout + B + Optional(arg)
checkout_command_b = git + checkout + b + Optional(arg)
clean_command_fd = git + clean + fd + Optional(arg)
clean_command_f = git + clean + f + Optional(arg)
reset_command_hard = git + reset + hard + Optional(arg)
reset_command_soft = git + reset + soft + Optional(arg)
reset_command_mixed = git + reset + mixed + Optional(arg)
rebase_command = git + rebase + Optional(arg)
rm_command_cached = git + rm + cached + Optional(arg)
rm_command = git + rm + Optional(arg)
stash_command_clear = git + stash + clear
stash_command_drop = git + stash + drop + Optional(arg)
commit_command_amend = git + commit + amend + Optional(arg)
merge_command = git + merge + Optional(arg)
fsck_command_full = git + fsck + full
gc_command_prune = git + gc + prune
reflog_command_expire = git + reflog + expire + all
update_ref_command_d = git + update_ref + Literal("-d") + Optional(arg)
filter_branch_command = git + filter_branch + Optional(arg)
filter_repo_command = git + filter_repo + Optional(arg)

destructive_commands = [
    push_command_force,
    push_command_f,
    branch_command_D,
    branch_command_d,
    checkout_command_B,
    checkout_command_b,
    clean_command_fd,
    clean_command_f,
    reset_command_hard,
    reset_command_soft,
    reset_command_mixed,
    rebase_command,
    rm_command_cached,
    rm_command,
    stash_command_clear,
    stash_command_drop,
    commit_command_amend,
    merge_command,
    fsck_command_full,
    gc_command_prune,
    reflog_command_expire,
    update_ref_command_d,
    filter_branch_command,
    filter_repo_command
]
