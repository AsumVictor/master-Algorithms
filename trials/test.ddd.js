const {addTwo} = require('./ddd');

test('adding', () => {
  expect(addTwo(3,8)).toBe(11);
});