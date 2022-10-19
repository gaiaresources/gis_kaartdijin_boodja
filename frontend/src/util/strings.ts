export function toCamelCase (string: string) {
  return string.toLowerCase().split(' ')
    .map((value, index) => index === 0 ? value : value.at(0)?.toUpperCase() + value.slice(1))
    .join('');
}
