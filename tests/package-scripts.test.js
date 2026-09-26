const test = require('node:test');
const assert = require('node:assert');
const fs = require('fs');
const path = require('path');

test('package.json contains expected scripts', async (t) => {
  const pkgPath = path.join(__dirname, '..', 'package.json');
  const pkgData = fs.readFileSync(pkgPath, 'utf8');
  const pkg = JSON.parse(pkgData);

  assert.ok(pkg.scripts, 'package.json should have a scripts object');

  const expectedScripts = {
    "skills:list": "skills add albertolicea00/agentskills -l",
    "skills:install": "skills add albertolicea00/agentskills",
    "skills:install:global": "skills add albertolicea00/agentskills -g",
    "skills:init": "skills init"
  };

  for (const [scriptName, scriptCommand] of Object.entries(expectedScripts)) {
    await t.test(`should have script ${scriptName}`, () => {
      assert.strictEqual(
        pkg.scripts[scriptName],
        scriptCommand,
        `Expected script '${scriptName}' to be '${scriptCommand}' but found '${pkg.scripts[scriptName]}'`
      );
    });
  }
});
