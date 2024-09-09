# Contribution Guidelines

## Issues
If you discover an issue with an algorithm, or test, open an issue to point out areas for improvement. 
If you are comfortable with it, implement the fix and open a PR.


## Adding tests
See the [testing contributors guide](tests/CONTRIBUTING.md)

## Coding Standards

### Languages

*GSQL*
- Follow the [GSQL Style Guide](https://docs.tigergraph.com/gsql-ref/current/appendix/gsql-style-guide)

*Python*
- Use the [ruff formatter](https://docs.astral.sh/ruff/formatter/#the-ruff-formatter) to format your code
- tests: pytest and networkx wherever applicable

*C/CPP*


## Pull Requests
- Make sure git knows your name and email address:
   ```
   $ git config user.name "J. Random User"
   $ git config user.email "j.random.user@example.com"
   ```
- The name and email address must be valid as we cannot accept anonymous contributions.
- Write good commit messages.
   - Concise commit messages that describe your changes help us better understand your contributions.

## General Guidelines

Ensure your pull request (PR) adheres to the following guidelines:

- Try to make the name concise and descriptive.
- Give a good description of the change being made. Since this is very subjective, see the [Updating Your Pull Request (PR)](#updating-your-pull-request-pr) section below for further details.
- Every pull request should be associated with one or more issues. If no issue exists yet, please create your own.
- Make sure that all applicable issues are mentioned somewhere in the PR description. This can be done by typing # to bring up a list of issues.

### Updating Your Pull Request (PR)

A lot of times, making a PR adhere to the standards above can be difficult. If the maintainers notice anything that we'd like changed, we'll ask you to edit your PR before we merge it. 
This applies to both the content documented in the PR and the changed contained within the branch being merged. There's no need to open a new PR. Just edit the existing one.

---

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

