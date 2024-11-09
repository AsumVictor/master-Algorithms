const sum = require('./challenge');

test('[1,3,6,8,4,5,9,4,3] target 6 should return [0, 4]', () => {
  expect(sum([1,3,6,8,4,5,9,4,3], 6)).toBe([0, 4]);
});

